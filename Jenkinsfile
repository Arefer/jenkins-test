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
            steps{
                def scannerHome = tool 'SonarScanner 4.0';
                withSonarQubeEnv('flask-sonarqube-server') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
    }
}