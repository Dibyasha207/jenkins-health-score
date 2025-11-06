pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/<your-username>/jenkins-health-score.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Health Scoring') {
            steps {
                echo 'Running health scoring script...'
                sh 'python3 score_health.py'
            }
        }

        stage('Report') {
            steps {
                echo 'Displaying final report...'
                sh 'cat reports/index.html'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}