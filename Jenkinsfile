pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull your code from GitHub
                git url: 'https://github.com/suchismitalenka103-blip/Seleniumpython.git', 
                    branch: 'main',
                    credentialsId: 'github-https-selenium'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Upgrade pip and install required packages

                 bat '"C:\\Users\\suchismita.lenka\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install --upgrade pip'
                 bat '"C:\\Users\\suchismita.lenka\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run Selenium tests
                bat 'python -m pytest --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            // Archive test report for Jenkins
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
    }
}
