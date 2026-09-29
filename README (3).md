<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Deploy a RAG API to Kubernetes

**Project Link:** [View Project](https://nextwork.ai/projects/c7d88b59-89df-52af-b9d7-13bf1777e1c8)

**Author:** Khaoula Belhadj  
**Email:** belhadjkhaoula07@gmail.com

---

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/c7d88b59-89df-52af-b9d7-13bf1777e1c8_y7z8a9b0)

## Introducing Today's Project!

In this project, I will deploy a RAG API to Kubernetes


### Key services and concepts

i'm expert abot k8d the new thing is RAG api 

### Challenges and wins

This project took me approximately 1:20min

### Why I did this project

I did this project because I wanted to learn deploy RAG API

## Setting Up My Docker Image

In this step, Before we deploy anything to Kubernetes, let's make sure you have a Docker image ready.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/c7d88b59-89df-52af-b9d7-13bf1777e1c8_i9j0k1l2)

### What the Docker image contains

runing cmd docker images 

## Installing Kubernetes Tools

In this step, I'm installing Minikube & kubectl.
Verify both tools are working.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/c7d88b59-89df-52af-b9d7-13bf1777e1c8_u1v2w3x4)

### Verifying the tools are installed

I installed Minikube using winget install -e --id Kubernetes.minikube I installed kubectl by winget install -e --id Kubernetes.kubectl .

## Starting My Kubernetes Cluster

In this step, I'm starting Minikube cluster.
Verify the cluster is running.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/c7d88b59-89df-52af-b9d7-13bf1777e1c8_g3h4i5j6)

### Loading the Docker image into Minikube

I started the cluster by running `minikube start` and saw the cluster start successfully. 

### Why load image into Minikube

needed to load my Docker image into Minikube because Minikube runs its own container environment and cannot automatically use images stored in my local Docker environment. Loading the image made it available inside the Minikube cluster, allowing Kubernetes to create pods and run my application without pulling the image from Docker Hub.

## Deploying to Kubernetes

In this step, I'm deploying my cluster

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/c7d88b59-89df-52af-b9d7-13bf1777e1c8_s5t6u7v8)

### How the Deployment keeps my app running

My deployment.yaml file defines how Kubernetes should deploy and manage my application. It specifies the Docker image to use, the number of pod replicas, and the container configuration such as the exposed port. Kubernetes uses this file to create the pods and keep the desired number of replicas running.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/c7d88b59-89df-52af-b9d7-13bf1777e1c8_a3b4c5d6)

### What did you observe when checking your pods?

I ran `kubectl get pods` and saw that my pod was listed with its name and status as `Running`, which means the pod was successfully created and is currently running. The `READY` column showed `1/1`, which indicates that the pod has one container and that container is ready to receive traffic.


## Creating a Service

In this step : 
Create a Kubernetes Service
Verify your Service is running

### What does the service.yaml file do?

The `service.yaml` file tells Kubernetes how to expose my application and provide stable network access to its Pods. The `selector` finds Pods by matching their labels. The port configuration allows the Service to forward traffic to the application running inside the Pods. `NodePort` enables access from outside the Kubernetes cluster by exposing the Service on a port of each node.


![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/c7d88b59-89df-52af-b9d7-13bf1777e1c8_m5n6o7p8)

### What kubectl commands did you run to create the service?

I applied my Service file by running `kubectl apply -f service.yaml`. I then verified that the Service was created by running `kubectl get services`.


## Accessing My API Through Kubernetes

In this step :
Access your API using NodePort
Test your API running in Kubernetes

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/c7d88b59-89df-52af-b9d7-13bf1777e1c8_y7z8a9b0)

### How I accessed my API

I tested my API by running an HTTP request against the Kubernetes Service using `Invoke-RestMethod`. The response showed that the API was reachable through the Kubernetes Service and returned the expected answer. This confirms that the Pod was running correctly, the Service was routing traffic to the Pod, and the application was functioning inside the Kubernetes cluster. The main difference between Docker and Kubernetes deployment is that Docker runs containers directly on a host, while Kubernetes manages and orchestrates containers using resources such as Pods, Deployments, and Services, providing scalability and automated management.


### Request flow through Kubernetes

The request flow went from my computer to the Kubernetes Node through the NodePort Service, then to the rag-app-service, and finally to the Pod running my RAG API container. The Service routed traffic by using label selectors to find the correct Pod and forward requests to it. NodePort enabled access by exposing the application on a port of the Kubernetes Node, allowing external requests to reach the API.

## Testing Self-Healing

In this project extension, I'll delete the pod and watch what happens.
See Kubernetes automatically create a replacement
Test that my API stayed available throughout

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/c7d88b59-89df-52af-b9d7-13bf1777e1c8_w8x9y0z1)

### What did you observe when you deleted the pod?

When I deleted the pod, I saw the status change from `Running` to `Terminating`, and shortly afterward a new pod appeared with the status `ContainerCreating` before changing to `Running`. A new pod was created because the Deployment continuously maintains the desired number of replicas. When the original pod was removed, Kubernetes automatically created a replacement pod to keep the application available.


![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/c7d88b59-89df-52af-b9d7-13bf1777e1c8_sm3j8k9l)

### How the Service routed traffic to the new pod

The Service automatically detected the new pod because it uses a selector that matches the labels of the pods managed by the Deployment. When the old pod was deleted, Kubernetes created a replacement pod with the same labels, so the Service automatically included it as a backend endpoint. Without Kubernetes, this would have required manually updating the application or load-balancer configuration. Self-healing is critical in production because it automatically replaces failed pods and helps keep applications available.


---

*Built with [NextWork](https://nextwork.ai) - [View this project](https://nextwork.ai/projects/c7d88b59-89df-52af-b9d7-13bf1777e1c8)*
