pipeline {
    agent any

    tools {
        // Убедитесь, что это имя СОВПАДАЕТ с Name в Global Tool Configuration
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
                // Игнорируем ошибки тестов через || true, чтобы дойти до генерации отчета
                sh './venv/bin/pytest --alluredir=allure-results || true'
            }
        }
    }

    post {
    always {
        allure includeProperties: false,
               jdk: 'java_home', // Имя, которое вы дали в настройках Tools
               results: [[path: 'allure-results']]
    }
}
}