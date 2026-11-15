
pipeline {
    agent any

    environment {
    PATH = "/Users/niswa/.docker/bin:/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin:${env.PATH}"
}

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test Application') {
            steps {
                sh 'PYTHONPATH=. .venv/bin/pytest -v'
            }
        }

        stage('Check Docker') {
            steps {
                sh 'which docker'
                sh 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-project-7:latest .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
                sh 'kubectl rollout status deployment/devops-app'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check console output.'
        }
    }
}
