import os

from fastapi import FastAPI, HTTPException
import chromadb

# Mock LLM mode for CI testing
# CI sets USE_MOCK_LLM=1
USE_MOCK_LLM = os.getenv("USE_MOCK_LLM", "0") == "1"

# Only import Ollama when running in production mode
if not USE_MOCK_LLM:
    import ollama

app = FastAPI()

# Use the same database path as build_knowledge_base.py
chroma = chromadb.PersistentClient(path="./db")
collection = chroma.get_or_create_collection("docs")


@app.post("/query")
def query(q: str):
    # Make sure the knowledge base contains documents
    if collection.count() == 0:
        raise HTTPException(
            status_code=503,
            detail="Knowledge base is empty. Run build_knowledge_base.py first.",
        )

    # Retrieve the most relevant document
    results = collection.query(
        query_texts=[q],
        n_results=1
    )

    documents = results.get("documents", [])

    if not documents or not documents[0]:
        raise HTTPException(
            status_code=404,
            detail="No relevant document found.",
        )

    context = documents[0][0]

    # CI mode: return retrieved text directly
    if USE_MOCK_LLM:
        return {
            "answer": context
        }

    # Production mode: use Ollama
    response = ollama.generate(
        model="tinyllama",
        prompt=(
            f"Context:\n{context}\n\n"
            f"Question: {q}\n\n"
            "Answer clearly and concisely:"
        )
    )

    return {
        "answer": response.response
    }