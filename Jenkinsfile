pipeline {
    agent any

    tools {
        // Убедитесь, что в Manage Jenkins -> Tools имя инструмента именно 'allure'
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
                // Добавляем очистку папки перед тестами, чтобы отчет был чистым
                sh 'rm -rf allure-results'
                // Запускаем тесты. Мы не боимся ошибки (exit code 1),
                // так как Allure соберет отчет в блоке post
                sh './venv/bin/pytest --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            script {
                // Генерация отчета
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}