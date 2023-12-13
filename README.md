# Sentiment Analysis FastAPI App
This project implements a Sentiment Analysis API using FastAPI and deploys it using Kubernetes. It consists of a FastAPI web application for sentiment analysis, a MySQL database to store predictions, and it can be easily deployed using Docker Compose and Kubernetes.

## Tools Used
FastAPI: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

MySQL: MySQL is used as the database to store sentiment predictions.

Docker Compose: Docker Compose is used for defining and running multi-container Docker applications.

Kubernetes: Kubernetes is used for orchestrating and deploying the application in a containerized environment.

HTML,CSS,Javascript: It is used to develop simple user interface.

## Project Structure

D:.
│   .env                         # Environment variables file
│   docker-compose.yml            # Docker Compose configuration
│   Dockerfile                    # Dockerfile for building the app image
│   kubernetes-deployment.yml     # Kubernetes deployment configuration
│   kubernetes-mysql-pvc.yml      # Kubernetes persistent volume claim configuration
│   kubernetes-mysql.yml          # Kubernetes MySQL deployment and service configuration
│   requirements.txt              # Python dependencies file
│   __init__.py                   # Empty file indicating that the directory should be treated as a Python package
│
└───app                          # Main application code directory
    │   database.py              # Database interaction module
    │   main.py                  # FastAPI application code
    │   __init__.py              # Empty file indicating that the directory should be treated as a Python package
    │
    ├───model                    # Directory for machine learning model
    │   │   model.py             # Model-related code
    │   │   sentiment_model.joblib  # Pre-trained sentiment analysis model
    │   │   __init__.py          # Empty file indicating that the directory should be treated as a Python package
    │
    ├───static                   # Directory for static files served by the app
    │       index.html           # HTML file for the main page
    │       negative-image.jpg   # Image file for negative sentiment
    │       positive-image.jpg   # Image file for positive sentiment
    │       script.js            # JavaScript file for frontend interactions
    │       sentiment-analysis-image.jpg  # Image file for sentiment analysis
    │       styles.css           # CSS file for styling
    │
    ├───templates                # Directory for HTML templates
    │       base.html            # Base HTML template

## Prerequisites
Docker Installed: Ensure Docker is installed on your system. Get Docker
Kubernetes Installed: For Kubernetes deployment, install Kubernetes, or use Minikube for local testing. Install Kubernetes with Minikube

Local Setup
1.Clone the repository:
```
git clone https://github.com/sathyark652/Sentiment-analysis-using-ai_mode-fastapi-docker-kubernetes.git
```
cd <project-directory>

2.Install project dependencies:
```
pip install -r requirements.txt
```
3.Set up environment variables:
Create a .env file and set the necessary environment variables. Refer to the provided .env for guidance.

4.Build and run the Docker container locally:

```
docker-compose build
docker-compose up
```
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/e5ce1603-e7d2-4918-a5e4-3cf06fc57018/1de54c13-4f1f-40a3-9aeb-be6dd6b59c54/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/e5ce1603-e7d2-4918-a5e4-3cf06fc57018/1de54c13-4f1f-40a3-9aeb-be6dd6b59c54/Untitled.png)

5.Access the application at http://localhost:8000.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/e5ce1603-e7d2-4918-a5e4-3cf06fc57018/576f4d18-d196-4772-bd9f-4ffa6878d944/Untitled.png)
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/e5ce1603-e7d2-4918-a5e4-3cf06fc57018/6d07d08b-6a58-49c4-9bd0-476659d1450d/Untitled.png)

## Kubernetes Deployment
Deploy the application on Kubernetes:

start minikube 

if you made your image private,do docker login first and build the latest image and push it to hub.
```
kubectl apply -f kubernetes-deployment.yml
kubectl apply -f kubernetes-mysql.yml
kubectl apply -f kubernetes-mysql-pvc.yml
```
check the pods and its service 
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/e5ce1603-e7d2-4918-a5e4-3cf06fc57018/32c1d5fa-2e67-445d-bc27-eaeb7f4a80f9/Untitled.png)


Access the deployed application after deploying using http://<EXTERNAL_IP>:PORT
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/e5ce1603-e7d2-4918-a5e4-3cf06fc57018/1a35ce14-5319-4870-abab-b57188fe796e/Untitled.png)

after deployment ,check whether its working right or not.

delete the pods and  stop the minikube.

For more detailed information, refer to the project's documentation and code files.

Note: Ensure all requirements from requirements.txt are installed locally if testing locally before deployment.


