pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-v /tmp:/tmp'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r streamlit1/requirements.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install flake8
                    flake8 streamlit1/ --count --select=E9,F63,F7,F82 --show-source --statistics
                '''
            }
        }

        stage('Test') {
            when {
                changeRequest()
            }
            steps {
                sh '''
                    . venv/bin/activate
                    cd streamlit1
                    pytest --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'streamlit1/test-results.xml'
                }
            }
        }

        stage('Build') {
            steps {
                sh '''
                    . venv/bin/activate
                    cd streamlit1
                    # Package application if needed
                    # For example: python -m build
                '''
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh '''
                    echo "Deploying application..."
                    # Add deployment steps here
                    # For example: scp or docker commands
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}