pipeline {
    agent any
    environment {
        PATH = "$PATH:/usr/local/bin"
    }
    stages {
        stage('Docker-compose') {
            steps{
                sh 'echo "building image and running container..."'
                sh 'docker-compose up -d'
                sh 'echo "app listening on port 5000"'
            }
        }
        stage('code analysis'){
            environment{
                scannerHome = tool 'sonar-scanner'
            }
            steps{
                withSonarQubeEnv('flask-sonarqube-server') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
    }
}