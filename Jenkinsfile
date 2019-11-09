pipeline {
    agent any
    environment {
        PATH = "$PATH:/usr/local/bin"
    }
    stages {
        stage('Start Docker'){
            steps{
                sh 'echo "Starting Docker daemon..."'
                sh 'open -a Docker'
            }
        }
        stage('Docker-compose') {
            steps{
                sh 'echo "building image and running container..."'
                sh 'docker-compose up'
                sh 'echo "app listening on port 5000"'
            }
        }
    }
}