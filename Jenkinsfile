pipeline {
    agent any

    tools {
        // Это связывает ваш установленный в Tools "allure" с пайплайном
        allure 'allure'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                // Используем python3 -m pip для надежности
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
                // Запускаем тесты через виртуальное окружение
                sh './venv/bin/pytest --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            // Теперь Jenkins знает, где искать исполняемый файл allure
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}