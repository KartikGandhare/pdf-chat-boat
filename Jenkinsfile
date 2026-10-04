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
               sh 'docker run --rm -v "$WORKSPACE:/app" -w /app python:3.14-slim sh -c "pip install -r requirements.txt && python -m pytest"'
             }
            
        }
    }

}
