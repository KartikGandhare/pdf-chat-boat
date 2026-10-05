pipeline {
    agent any
    stages{
        stage('Checkout'){
            steps{
                checkout scm
            }
        }
        stage('Test'){
            steps{
               sh 'docker run --rm -v "$WORKSPACE:/app" -w /app python:3.14-slim sh -c "pip install -r requirements.txt && python -m pytest tests/"'
             }
            
        }
        stage('Build Docker Images'){
            steps{
                sh 'docker build -t pdf-chat-boat-backend:test .'
                sh 'docker build -t pdf-chat-boat-frontend:test -f frontend/Dockerfile .'

            }
        }
    }

}
