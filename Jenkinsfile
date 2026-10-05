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
        stage('Push Docker Images'){
            steps{
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]){
                    sh 'echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin'
                    sh 'docker tag pdf-chat-boat-backend:test $DOCKER_USERNAME/pdf-chat-boat-backend:latest'
                    sh 'docker tag pdf-chat-boat-frontend:test $DOCKER_USERNAME/pdf-chat-boat-frontend:latest'
                    sh 'docker push $DOCKER_USERNAME/pdf-chat-boat-backend:latest'
                    sh 'docker push $DOCKER_USERNAME/pdf-chat-boat-frontend:latest'
                    }
            }
        }
    }

}
