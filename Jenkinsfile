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
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Data Ingestion') {
            steps {
                sh 'python src/ingestion.py'
            }
        }

        stage('Data Profiling & Quality Analysis') {
            steps {
                sh 'python src/profiling.py'
                sh 'python src/quality_analysis.py'
            }
        }

        stage('Automated Data Repair') {
            steps {
                sh 'python src/data_repair.py'
            }
        }

        stage('Model Training') {
            steps {
                sh 'python src/train.py'
            }
        }

        stage('Model Validation') {
            steps {
                sh 'python src/validate.py'
            }
        }

        stage('Model Testing') {
            steps {
                sh 'python src/test.py'
            }
        }

        stage('Deployment Ready') {
            steps {
                echo 'Model passed all quality gates and is deployment-ready'
            }
        }
    }
}