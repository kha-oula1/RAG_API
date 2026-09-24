from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import os
import ollama
import chromadb
from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction,
)

app = FastAPI()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

client = chromadb.PersistentClient(path="./chroma_db")

ef = OllamaEmbeddingFunction(
    model_name="nomic-embed-text",
    url=OLLAMA_URL,
)

collection = client.get_or_create_collection(
    name="personal_profile",
    embedding_function=ef,
)

# Load Kubernetes knowledge without embedding it during module import. The API
# can start even when Ollama is temporarily unavailable.
with open("k8s.txt", "r", encoding="utf-8") as f:
    k8s_text = f.read()


def ensure_k8s_knowledge() -> None:
    existing = collection.get(ids=["k8s-knowledge"])["ids"]
    if existing:
        return

    try:
        collection.upsert(
            ids=["k8s-knowledge"],
            documents=[k8s_text],
            metadatas=[{"source": "k8s"}],
        )
    except ConnectionError as exc:
        raise HTTPException(
            status_code=503,
            detail=(
                "Ollama is unavailable. Start Ollama and ensure "
                f"'{OLLAMA_URL}' is reachable."
            ),
        ) from exc


class DocumentSubmission(BaseModel):
    user_name: str
    content: str


@app.post("/documents")
def add_document(submission: DocumentSubmission):
    chunks = [
        chunk.strip()
        for chunk in submission.content.split("\n\n")
        if chunk.strip()
    ]

    collection.add(
        ids=[
            f"{submission.user_name}-chunk{i}"
            for i in range(len(chunks))
        ],
        documents=chunks,
        metadatas=[
            {
                "source": "profile",
                "user_name": submission.user_name,
                "chunk_index": i,
            }
            for i in range(len(chunks))
        ],
    )

    return {
        "message": f"Added {len(chunks)} chunks for user '{submission.user_name}'.",
        "user_name": submission.user_name,
        "chunks_added": len(chunks),
    }


@app.post("/query")
def query(q: str):
    ensure_k8s_knowledge()
    results = collection.query(
        query_texts=[q],
        n_results=1,
        where={"source": "k8s"},
    )

    context = ""

    if results["documents"] and results["documents"][0]:
        context = results["documents"][0][0]

    ollama_client = ollama.Client(host=OLLAMA_URL)

    answer = ollama_client.generate(
        model="tinyllama",
        prompt=f"""Use the following Kubernetes context to answer the question.

Context:
{context}

Question: {q}

Answer clearly and concisely:""",
    )

    return {
        "question": q,
        "answer": answer["response"],
        "context_used": context,
    }


@app.get("/ask")
def ask(question: str, user: str = None):
    ensure_k8s_knowledge()
    query_params = {
        "query_texts": [question],
        "n_results": 2,
    }

    if user:
        query_params["where"] = {
            "source": "profile",
            "user_name": user,
        }

    results = collection.query(**query_params)

    context = "\n\n".join(results["documents"][0])

    augmented_prompt = f"""Use the following context to answer the question.
If the context doesn't contain relevant information, say so.

Context:
{context}

Question: {question}"""

    ollama_client = ollama.Client(host=OLLAMA_URL)

    response = ollama_client.chat(
        model="qwen2.5:0.5b",
        messages=[
            {
                "role": "user",
                "content": augmented_prompt,
            }
        ],
    )

    return {
        "question": question,
        "answer": response["message"]["content"],
        "context_used": results["documents"][0],
        "filtered_by_user": user,
    }

