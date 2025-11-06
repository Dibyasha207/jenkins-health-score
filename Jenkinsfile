pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo '📥 Cloning repository...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo '🏗 Building the project...'
                // Simulate build steps (you can replace this with real commands)
                sh 'echo "Build successful!"'
            }
        }

        stage('Health Scoring') {
            steps {
                echo '💡 Running health and security scoring...'
                sh '''
                mkdir -p reports
                echo "Build Health: 95%" > reports/health.txt
                echo "Security Score: 82%" >> reports/health.txt
                echo "Overall Rating: Good" >> reports/health.txt
                '''
            }
        }

        stage('Report') {
            steps {
                echo '📝 Generating HTML Report...'
                sh '''
                mkdir -p reports
                echo "<html><head><title>Jenkins Health Report</title></head><body>" > reports/index.html
                echo "<h1 style='color:#2E8B57;'>Jenkins Health and Security Score Report</h1>" >> reports/index.html
                echo "<h3>Build Health: 95%</h3>" >> reports/index.html
                echo "<h3>Security Score: 82%</h3>" >> reports/index.html
                echo "<h3>Overall Rating: Good</h3>" >> reports/index.html
                echo "<p>Generated automatically by Jenkins Pipeline ✅</p>" >> reports/index.html
                echo "</body></html>" >> reports/index.html
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'

            // Publish HTML report inside Jenkins UI
            publishHTML(target: [
                reportDir: 'reports',
                reportFiles: 'index.html',
                reportName: 'Health and Security Report'
            ])
        }

        failure {
            echo '❌ Pipeline failed. Please check error logs.'
        }
    }
}