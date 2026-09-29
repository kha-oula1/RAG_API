<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Containerize a RAG API with Docker

**Project Link:** [View Project](https://nextwork.ai/projects/1d9c4e8d-5bfc-5802-9aee-71f75545344b)

**Author:** Khaoula Belhadj  
**Email:** belhadjkhaoula07@gmail.com

---

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/1d9c4e8d-5bfc-5802-9aee-71f75545344b_x7y8z9a0)

## Introducing Today's Project!

In this project, I will containerize a RAG API with Docker


### Key services and concepts

The services and tools I used were FastAPI, Ollama, ChromaDB, Docker, and Docker Hub.

Key concepts I learnt include RAG (Retrieval-Augmented Generation), embeddings, vector databases, API development with FastAPI, connecting an LLM to a knowledge base, Docker containerization, Docker images and containers, and pushing and pulling images from Docker Hub.

I also learnt how to connect a containerized application to services running outside the container and how containerization makes applications more portable and easier to deploy.

### Challenges and wins

This project took me approximately 30min

### Why I did this project

I did this project because wanna learn RAG API

## Setting Up the RAG API

In this step, I'm setting up RAG API's code, database and dependencies.
Set up your virtual environment.
Run Ollama.

### API setup and workspace

In this step, Install Docker Desktop.

### Dependencies installed

I installed several Python packages for this project:
FastAPI — used to build the REST API and create endpoints such as /ask and /documents.
Uvicorn — used to run the FastAPI application as a web server.
ChromaDB — used as the vector database to store document chunks and embeddings and retrieve relevant information.
Ollama — used to communicate with local AI models and generate responses.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/1d9c4e8d-5bfc-5802-9aee-71f75545344b_c9d0e1f2)

### Local API working

I tested the API using the Swagger UI provided by FastAPI. I first used the POST /documents endpoint to add a user profile and verified that the API returned a successful 200 response with the number of chunks added. Then, I used the GET /ask endpoint with a question and the user's name to verify that the API could retrieve the correct profile information and generate an answer using the RAG system.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/1d9c4e8d-5bfc-5802-9aee-71f75545344b_v5w6x7y8)

## Installing Docker Desktop

### Docker Desktop setup

Docker Desktop is a tool that allows developers to build, run, and manage Docker containers on their computer. I installed it because I needed a container environment to run and test my RAG API and its services consistently. Containerization will help my project by making the application easier to deploy, isolate dependencies, reproduce the same environment on different machines, and later run the API with Kubernetes.

### Docker verification

I verified Docker is working by using commande docker run "......."

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/1d9c4e8d-5bfc-5802-9aee-71f75545344b_i9j0k1l2)

## Creating the Dockerfile

In this step, I'm creating a Dockerfile for my RAG API
Build a Docker image of my RAG API
Test your containerized API

### How the Dockerfile works

A Dockerfile is a text file that contains instructions for building a Docker image. My Dockerfile defines the environment needed to run my RAG API. It starts from a Python base image, installs the required Python packages, copies my application files into the container, exposes the API port, and defines the command to start the FastAPI application with Uvicorn. This allows my RAG API to run consistently inside a Docker container without depending on my local Python environment.

### Containerized API test results

Testing the API after containerization proved that the RAG API could run successfully inside a Docker container and still communicate with Ollama, ChromaDB, and the Kubernetes knowledge base to generate answers.
Containerization helps because it makes the application more portable, consistent, and easier to deploy on another machine without manually installing all the Python dependencies and configuration.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/1d9c4e8d-5bfc-5802-9aee-71f75545344b_o1p2q3r4)

## Building and Running the Container

### Docker image build complete

I verified my Docker image was built successfully by commande docker images

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/1d9c4e8d-5bfc-5802-9aee-71f75545344b_p9q0r1s2)

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/1d9c4e8d-5bfc-5802-9aee-71f75545344b_x7y8z9a0)

## Pushing to Docker Hub

Tag my image for Docker Hub
Push myimage to Docker Hub
Pull and run my image from Docker Hub

### Docker Hub push complete

I pushed my Docker image to Docker Hub by first logging in with docker login, then tagging my local image with my Docker Hub repository name using docker tag, and finally uploading it with docker push.
The main advantages are that Docker Hub provides a centralized place to store and share container images. It makes the application easier to distribute, deploy on other machines, and use in CI/CD pipelines without rebuilding the image from scratch

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/1d9c4e8d-5bfc-5802-9aee-71f75545344b_m5n6o7p8)

### Pulling from Docker Hub

Pulling an image from Docker Hub means downloading a previously built Docker image from a remote repository to my local machine.
When I ran docker pull, Docker downloaded the image layers from Docker Hub and recreated the image locally so I could run it as a container.
The difference between building locally and pulling from Docker Hub is that building creates the image from a Dockerfile and application files on my machine, while pulling downloads an already-built image. Pulling is faster and allows me to use the same tested image without rebuilding it.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/1d9c4e8d-5bfc-5802-9aee-71f75545344b_f5g6h7i8)

---

*Built with [NextWork](https://nextwork.ai) - [View this project](https://nextwork.ai/projects/1d9c4e8d-5bfc-5802-9aee-71f75545344b)*
