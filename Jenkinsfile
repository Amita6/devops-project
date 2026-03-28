pipeline {
    agent any

    environment {
        IMAGE_NAME = C:\Users\ASUS\OneDrive\Desktop\devops-project"
    }

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/Amita6/devops-project.git'
            }
        }

        stage('Lint') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 app/'
            }
        }

        stage('Test') {
            steps {
                sh 'pip install -r app/requirements.txt pytest'
                sh 'pytest app/test_app.py'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose up -d'
            }
        }
    }
}