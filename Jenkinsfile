pipeline {
    agent any

    stages {
        stage('Checkout') {
            git "https://github.com/Arefer/jenkins-test"
        }
        stage('Docker-compose') {
            sh 'echo "building image and running container...""'
            sh 'docker-compose up'
            sh 'app listening on port 5000'
        }
    }
}