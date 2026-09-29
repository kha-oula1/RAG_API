import os
import chromadb

# Initialize ChromaDB
client = chromadb.PersistentClient(path="./db")

# Use the same collection as main.py
collection = client.get_or_create_collection("docs")

# Documents inside the docs folder
documents = [
    ("docs/k8s.txt", "k8s"),
    ("docs/nextwork.txt", "nextwork"),
]

all_chunks = []
all_ids = []
all_metadatas = []

for filepath, source in documents:
    if not os.path.exists(filepath):
        print(f"WARNING: {filepath} not found")
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = [
        chunk.strip()
        for chunk in text.split("\n\n")
        if chunk.strip()
    ]

    print(f"Loaded {len(chunks)} chunks from {filepath}")

    for i, chunk in enumerate(chunks):
        all_chunks.append(chunk)
        all_ids.append(f"{source}-chunk{i}")
        all_metadatas.append({
            "source": source,
            "chunk_index": i
        })

if not all_chunks:
    raise RuntimeError("No documents were loaded.")

collection.upsert(
    ids=all_ids,
    documents=all_chunks,
    metadatas=all_metadatas,
)

print(f"Added {len(all_chunks)} chunks to the 'docs' collection.")
print("Knowledge base built successfully!")