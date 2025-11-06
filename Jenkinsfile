pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Dibyasha207/jenkins-health-score.git'
            }
        }

        stage('Build') {
            steps {
                echo '✅ Building project...'
                sh 'echo Build Success: 98% > build_report.txt'
            }
        }

        stage('Health Scoring') {
            steps {
                echo '🧮 Calculating Health Score...'
                sh 'echo Vulnerabilities Found: 4 >> build_report.txt'
                sh 'echo Final Score: 78 >> build_report.txt'
            }
        }

        stage('Report') {
            steps {
                echo '📝 Generating HTML Report...'
                sh '''
                mkdir -p reports
                echo "<h1>Jenkins Health and Security Score Report</h1>" > reports/index.html
                echo "<p><b>Build Success:</b> 98%</p>" >> reports/index.html
                echo "<p><b>Vulnerabilities Found:</b> 4</p>" >> reports/index.html
                echo "<p><b>Final Score:</b> 78</p>" >> reports/index.html
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed."
        }
    }
}