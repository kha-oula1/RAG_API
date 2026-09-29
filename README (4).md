<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Automate Testing with GitHub Actions

**Project Link:** [View Project](https://nextwork.ai/projects/52eea278-7fe7-53be-b1cd-7c415b7dccbb)

**Author:** Khaoula Belhadj  
**Email:** belhadjkhaoula07@gmail.com

---

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/52eea278-7fe7-53be-b1cd-7c415b7dccbb_i1j2k3l4)

## Introducing Today's Project!

In this project, I will automate testing with GitHub Actions

### Key services and concepts

The key services I used were **FastAPI, ChromaDB, Ollama, Docker, GitHub, and GitHub Actions**. The main concepts I learnt include **RAG, semantic search, embeddings, vector databases, API development, Docker containerization, CI/CD, automated testing, and Mock LLM testing**. I also learnt how to organize documents in a `docs` folder, build a knowledge base, test retrieval quality, and use CI to automatically validate changes.


### Challenges and wins

This project took me approximately 1:30min

### Why I did this project

I did this project because I wanted to learn implements mock llm

## Setting Up Your RAG API

Set up your RAG API's code, database and dependencies.
Test your RAG API locally.

### Local API verification

I verified my RAG API by running the FastAPI application locally with Uvicorn and testing the API endpoints through the browser and API documentation. I submitted questions to the API and confirmed that it retrieved relevant information from the embedded knowledge base before generating responses. I also checked the logs to ensure requests were processed successfully and that the API returned valid JSON responses.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/52eea278-7fe7-53be-b1cd-7c415b7dccbb_i9j0k1l2)

## Initializing Git and Pushing to GitHub

Set up Git in your project
Create a GitHub repository
Push your code to GitHub

### Git initialization and first commit

I initialized Git by creating a new Git repository in my project directory using git init. Then, I staged all the project files with git add . and created my first commit using git commit -m "Initial commit".

The .gitignore file helps by preventing unnecessary files and folders, such as virtual environments, cache files, and system-generated files, from being tracked by Git. This keeps the repository clean and focused on the source code and important project files.

### Pushing to GitHub for CI/CD

Pushing to GitHub means uploading my local code and commit history from my computer to a remote GitHub repository. This creates a centralized version of the project that can be accessed, tracked, and collaborated on from anywhere.

This enables CI/CD because tools such as GitHub Actions, Jenkins, or other automation platforms can detect new commits and automatically trigger pipelines. After a push, the pipeline can build the application, run tests, create Docker images, and deploy updates without requiring manual intervention. This helps ensure that code changes are validated and delivered consistently and efficiently.


![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/52eea278-7fe7-53be-b1cd-7c415b7dccbb_y5z6a7b8)

## Creating Semantic Tests

Create semantic tests for your RAG API.
Run tests locally and see tests pass.
Experiment with breaking and fixing your knowledge base.
Test your API repeatedly and observe interesting behavior.

### Non-deterministic output observation

When I ran the same query multiple times, I observed that the API returned similar answers each time, although the exact wording could vary slightly. This shows that the RAG system consistently retrieves relevant information for the same question, while the generated response may not always be identical.


## Adding Mock LLM Mode

I'm adding mock LLM mode and test it 

### Mock LLM mode for CI testing

Mock LLM mode returns the retrieved text directly, which makes tests fast, deterministic, and independent of an actual LLM service. Without mock mode, tests would depend on the availability of the LLM, take longer to run, and may produce different responses for the same query. For automated CI, we need reliable and repeatable tests that can run without external dependencies, API calls, or model servers such as Ollama.

## Creating GitHub Actions Workflow

I'm creating a GitHub Actions workflow file .

### Workflow automation and CI testing

I created the workflow file in the .github/workflows/ directory of my Git repository .github/workflows/ci.yml. I defined the workflow steps to build and test my application automatically. I pushed it using Git commands:

## Testing Data Quality

Trigger your GitHub Actions workflow
Watch GitHub Actions automatically test your code
Observe the workflow fail due to data quality issues

### Data quality and CI protection

The missing keyword was "orchestration" in the Kubernetes knowledge base content. The semantic test failed because the API response did not contain the expected Kubernetes-related terms, indicating that the retrieved knowledge was incomplete or degraded.

Without CI, this degraded content would have been added to the knowledge base and deployed without detection, leading to lower-quality answers from the RAG system. The automated semantic test protected the knowledge base by identifying the issue early and preventing changes that could reduce the accuracy and usefulness of responses.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/52eea278-7fe7-53be-b1cd-7c415b7dccbb_i1j2k3l4)

## Testing Another Data Quality Issue

## Scaling with Multiple Documents

I'm restructuring the project

### Docs folder structure and CI scaling

The `docs` folder organizes files by **document type or topic**, such as `k8s.txt` and `nextwork.txt`. The `build_knowledge_base.py` script handles **loading these documents, splitting them into chunks, and storing them in the ChromaDB knowledge base**. CI validated the documents and found **issues such as missing or incorrect knowledge content through semantic tests**. This structure supports growth by **making it easy to add more documents without changing the main RAG API code**.


![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/52eea278-7fe7-53be-b1cd-7c415b7dccbb_g5h6i7j8)

---

*Built with [NextWork](https://nextwork.ai) - [View this project](https://nextwork.ai/projects/52eea278-7fe7-53be-b1cd-7c415b7dccbb)*
