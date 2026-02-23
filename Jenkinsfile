pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/AARAV-git/azure-ml-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Data Ingestion') {
            steps {
                bat 'python src/ingestion.py'
            }
        }

        stage('Data Profiling & Quality Analysis') {
            steps {
                bat 'python src/profiling.py'
                bat 'python src/quality_analysis.py'
            }
        }

        stage('Automated Data Repair') {
            steps {
                bat 'python src/data_repair.py'
            }
        }

        stage('Model Training') {
            steps {
                bat 'python train.py'
            }
        }

        stage('Model Validation') {
            steps {
                bat 'python src/validate.py'
            }
        }

        stage('Model Testing') {
            steps {
                bat 'python src/test.py'
            }
        }

        stage('Deployment Ready') {
            steps {
                echo 'Model passed all quality gates and is deployment-ready'
            }
        }
    }
}