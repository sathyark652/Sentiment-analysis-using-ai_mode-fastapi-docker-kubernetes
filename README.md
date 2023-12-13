# Sentiment Analysis FastAPI App
This project implements a Sentiment Analysis API using FastAPI and deploys it using Kubernetes. It consists of a FastAPI web application for sentiment analysis, a MySQL database to store predictions, and it can be easily deployed using Docker Compose and Kubernetes.

![image](https://github.com/sathyark652/Sentiment-analysis-using-ai_mode-fastapi-docker-kubernetes/assets/117423140/1f629774-d5a3-479c-88cb-231fd6174529)

## Tools Used
FastAPI: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

MySQL: MySQL is used as the database to store sentiment predictions.

Docker Compose: Docker Compose is used for defining and running multi-container Docker applications.

Kubernetes: Kubernetes is used for orchestrating and deploying the application in a containerized environment.

HTML,CSS,Javascript: It is used to develop simple user interface.

## Workflow
fastapi authentication
![image](https://github.com/sathyark652/Sentiment-analysis-using-ai_mode-fastapi-docker-kubernetes/assets/117423140/88a2cd1a-a8ab-4ecc-8e3b-ef7efb36eb96)

so authentication is successful and fastapi is working
![image](https://github.com/sathyark652/Sentiment-analysis-using-ai_mode-fastapi-docker-kubernetes/assets/117423140/942e3bce-9822-4162-8564-229ac0e9195f)

fastapi apipoints: (access at http://127.0.0.1:8000/docs)
![image](https://github.com/sathyark652/Sentiment-analysis-using-ai_mode-fastapi-docker-kubernetes/assets/117423140/f97530d6-fdf2-4ccd-995c-7d0e5a6602c7)

frontend for user input and prediction of output:

![image](https://github.com/sathyark652/Sentiment-analysis-using-ai_mode-fastapi-docker-kubernetes/assets/117423140/d1467c9d-4b8a-4ab8-a42b-fc8a19d08a87)


## Project Structure
```
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
```
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
![image](https://github.com/sathyark652/Sentiment-analysis-using-ai_mode-fastapi-docker-kubernetes/assets/117423140/3cb66c18-437f-4333-8877-40cca7b01bab)


5.Access the application at http://localhost:8000.

![image](https://github.com/sathyark652/Sentiment-analysis-using-ai_mode-fastapi-docker-kubernetes/assets/117423140/44b8733c-b3c4-48b5-ab9a-b43698b85d8d)


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

![image](https://github.com/sathyark652/Sentiment-analysis-using-ai_mode-fastapi-docker-kubernetes/assets/117423140/7a17d0ed-5526-494e-b0f0-117e0555dd16)

Access the deployed application after deploying using http://<EXTERNAL_IP>:PORT(ex: http://127.0.0.1:30335/docs#/default/predict_predict_post)

![image](https://github.com/sathyark652/Sentiment-analysis-using-ai_mode-fastapi-docker-kubernetes/assets/117423140/500d2f94-478c-4c7e-9589-322130522d5e)

after deployment ,check whether its working right or not.

delete the pods and  stop the minikube.

For more detailed information, refer to the project's documentation and code files.

Note: Ensure all requirements from requirements.txt are installed locally if testing locally before deployment.


