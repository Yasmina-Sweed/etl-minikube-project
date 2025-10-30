## ETL Pipeline on Minikube using Docker & Kubernetes
📘 Overview
This project demonstrates how to deploy a simple ETL (Extract, Transform, Load) job on Minikube, using Docker and Kubernetes.
The pipeline extracts data (simulated via a Python script), transforms it, and loads it into a PostgreSQL database — all running on a local Kubernetes cluster.

🧩 Project Structure
.
├── Dockerfile
├── etl.py
├── etl-job.yaml
├── postgres-deployment.yaml
└── README.md

Dockerfile → Builds the ETL job image.
etl.py → Python script that performs the ETL logic.
etl-job.yaml → Kubernetes Job that runs the ETL container.
postgres-deployment.yaml → Deploys a PostgreSQL database in the cluster.
README.md → Documentation of the steps and purpose.


⚙️ Setup Steps
1️⃣ Start Minikube
minikube start
2️⃣ Build Docker Image inside Minikube
Since Minikube has its own Docker environment, run:
minikube ssh
docker build -t etl-job:latest /path/to/project
exit
3️⃣ Deploy PostgreSQL
kubectl apply -f postgres-deployment.yaml
Verify the pod is running:
kubectl get pods
4️⃣ Deploy the ETL Job
kubectl apply -f etl-job.yaml
Check logs to confirm the ETL ran successfully:
kubectl logs job/etl-job
5️⃣ Verify Results
You can connect to the PostgreSQL pod and check that data was loaded:
kubectl exec -it <postgres-pod-name> -- psql -U postgres

💡 Notes

You can rebuild the ETL image anytime with:

bashminikube ssh
docker rmi etl-job:latest
docker build -t etl-job:latest /path/to/project

To remove the job:

bashkubectl delete job etl-job

To redeploy after editing:

bashkubectl apply -f etl-job.yaml

🌟 Purpose of This Project
This setup is a training project to understand how containerized ETL workflows run in a Kubernetes environment.
It demonstrates core DevOps and Data Engineering skills — Docker image creation, YAML configuration, and orchestration with Minikube.

🧰 Tools Used

Python 3
Docker
Kubernetes (Minikube)
PostgreSQL

