<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Build a RAG API with FastAPI

**Project Link:** [View Project](https://nextwork.ai/projects/99ec4595-3d7b-5584-a799-aafb9c373bbb)

**Author:** Khaoula Belhadj  
**Email:** belhadjkhaoula07@gmail.com

---

## Introducing Today's Project!

In this project, I'm going to build a local AI pipeline that retrieves, augments, and generates answers from my own documents.

### Key tools and concepts

The key tools I used include Uvicorn server (currently running).
Python virtual environment.
ChromaDB data directory (./chroma_db).
Project files (rag-api directory).

### Challenges and wins

This project took me approximately 30min

## Performing RAG Manually

In this step, I'm going to See RAG in action with a manual demo.
Set up a Python project with a virtual environment.
Install all project dependencies.
Pull the nomic-embed-text embedding model.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/99ec4595-3d7b-5584-a799-aafb9c373bbb_v3j7x5b9)

### Understanding the three parts of RAG

I performed RAG manually by the three parts are Retrieval → Augmentation → Generation

### Comparing the two AI models

The key difference I noticed is it doesn't chat like qwen2.5:0.5b , it converts text into numbers for search. 

## Building a Personal Knowledge Base

In this step, I'm going to write a personal profile document.
Build a Python script that loads, chunks, and stores your profile as embeddings.
Run the script and verify your knowledge base is built.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/99ec4595-3d7b-5584-a799-aafb9c373bbb_g3h7m2r5)

### Creating the profile document

The information helps the AI answer questions about you because it provides external knowledge that can be retrieved and supplied to the model when needed.

### How semantic search finds relevant chunks

ChromaDB finds the most relevant chunks using vector similarity search.

## Creating the RAG API with FastAPI

In this step, I'm going to build an API with fastapi and /ask end point  I'll test it using swagger UI

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/99ec4595-3d7b-5584-a799-aafb9c373bbb_j5m1r8t2)

### How the /ask endpoint works

So the /ask endpoint performs:
Retrieve relevant information from ChromaDB.
Augment the prompt with that information.
Generate an answer using the language model.

### Testing with Swagger UI

I tested my API by asking, **“What’s my name?”** through the Swagger UI. The AI answered with my name, "Khaoula Belhadj". The context used was the relevant information retrieved from my "profile.txt" through ChromaDB. The RAG system retrieved the profile chunk containing my name, added it to the prompt, and the AI used that context to generate the answer.


## Extending to a Multi-User AI Directory

Adding multi-user support teaches you dynamic document ingestion, metadata filtering in vector databases, and basic multi-tenancy patterns. 

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/99ec4595-3d7b-5584-a799-aafb9c373bbb_d5g9k3n7)

### Adding the POST /documents endpoint

In this project extension, I added a POST /documents endpoint that stores user-specific documents in ChromaDB as text chunks, along with metadata identifying the user. Metadata filtering allows the /ask endpoint to retrieve only the documents belonging to the current user, so each user can have a separate knowledge base and receive answers based on their own information.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/99ec4595-3d7b-5584-a799-aafb9c373bbb_r8t2w6y1)

### Verifying multi-user filtering

In this project extension, I tested multi-user queries by adding Jordan’s profile to the knowledge base and then asking questions using the `user` parameter. I verified that a query for Jordan retrieves information only from Jordan’s profile, such as his hobbies and career goals. The filter works because ChromaDB uses the user metadata to retrieve only the chunks associated with the specified user, preventing information from other users’ profiles from being included.


## Wrapping Up

I did this project today to learn how to build a RAG API that combines FastAPI, ChromaDB, and Ollama. I learned how to create a knowledge base, store documents as embeddings, retrieve relevant information using vector similarity, and use an LLM to generate answers based on the retrieved context. I also learned how to implement user-specific data and metadata filtering so that each user’s information remains separated when answering questions.


---

*Built with [NextWork](https://nextwork.ai) - [View this project](https://nextwork.ai/projects/99ec4595-3d7b-5584-a799-aafb9c373bbb)*
