pipeline {
    agent any
    environment {
        PATH = "$PATH:/usr/local/bin/docker-compose"
    }
    stages {
        stage('Checkout') {
            steps {
                git "https://github.com/Arefer/jenkins-test"
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