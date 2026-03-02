pipeline {
    agent any

    tools {
        allure 'allure'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                    ./venv/bin/playwright install --with-deps
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'rm -rf allure-results'
                sh './venv/bin/pytest --alluredir=allure-results || true'
            }
        }
    }

    post {
    always {
        allure includeProperties: false,
               jdk: 'java_home',
               results: [[path: 'allure-results']]
    }
}
}