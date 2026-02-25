pipeline {
    agent any

    environment {
        // Убедитесь, что Python 3.10 доступен в PATH
        PATH = "/usr/bin/python3.10:$PATH"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'playwright install --with-deps'
            }
        }

        stage('Run Tests') {
            steps {
                // Добавляем флаг --alluredir для сохранения результатов
                sh 'pytest --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            // Генерация Allure отчета
            // results: путь к папке, которую создал pytest
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}