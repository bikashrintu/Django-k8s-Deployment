# 🚗 Carvilla - Django App Deployment on Kubernetes

This repository contains the configuration and setup to deploy the **Carvilla Django web application** using **Docker** and **Kubernetes (Minikube)**.

---

## 📦 Project Overview

- **Framework**: Django (Python)
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Platform**: Minikube (running on AWS EC2 or local machine)

---

## 🗂 Project Structure

carvilla-k8s-deployment/
├── Dockerfile                 # Dockerfile for building Django app image
├── requirements.txt           # Python dependencies
├── kubernetes/
│   ├── deployment.yaml        # Kubernetes Deployment configuration
│   ├── service.yaml           # Kubernetes Service to expose the app
│   └── configmap.yaml         # (Optional) ConfigMap for environment configs
├── manage.py                  # Django management script
├── carvilla/                  # Main Django project folder
│   ├── settings.py            # Django settings
│   └── urls.py                # URL routing
└── README.md                  # Project documentation
