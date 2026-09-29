import chromadb

# Load the Kubernetes knowledge document
with open("k8s.txt", "r") as f:
    text = f.read()

# Split into chunks by paragraph - each blank line becomes a split point
# strip() removes extra whitespace, and the if-check skips empty chunks
chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

print(f"Loaded {len(chunks)} chunks from k8s.txt")

# Initialize the same ChromaDB store used by the API
client = chromadb.PersistentClient(path="./db")

# Create (or reuse) the collection used by the API
collection = client.get_or_create_collection(
    name="docs",
)

# Add chunks to the collection - ChromaDB automatically generates embeddings
collection.upsert(
    ids=[f"chunk{i}" for i in range(len(chunks))],  # Unique ID for each chunk
    documents=chunks,  # The actual text content
    metadatas=[{"source": "k8s", "chunk_index": i} for i in range(len(chunks))],
)

print(f"Added {len(chunks)} chunks to the 'docs' collection.")
print("Knowledge base built successfully!")
