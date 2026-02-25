pipeline {
    agent any

    environment {
        ALLURE_RESULTS = 'allure-results'
        PATH = "/usr/local/opt/python@3.10/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Prepare Environment') {
            steps {
                script {
                    sh '''
                        python3.10 -m venv venv
                        source venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Install Playwright') {
            steps {
                sh '''
                    source venv/bin/activate
                    playwright install chromium --with-deps
                '''
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh "mkdir -p ${ALLURE_RESULTS}"
                    sh '''
                        source venv/bin/activate
                        pytest --alluredir=${ALLURE_RESULTS} || true
                    '''
                }
            }
        }
    }

    post {
        always {
            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'allure-results']]
        }
    }
}