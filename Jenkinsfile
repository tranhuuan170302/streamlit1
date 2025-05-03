pipeline {
    agent any

    stages {
        stage('Checkout PR') {
            steps {
                // Checkout code từ Pull Request mà không cần credentials
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    // Cài đặt môi trường ảo và yêu cầu nếu cần thiết
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Lint') {
            steps {
                // Lint code để đảm bảo không có lỗi cú pháp
                sh '''
                    . venv/bin/activate
                    pip install flake8
                    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                '''
            }
        }

        stage('Build') {
            steps {
                // Bước build ứng dụng nếu cần
                sh '''
                    . venv/bin/activate
                    echo "Building application..."
                    python3 app.py
                '''
            }
        }
    }

    post {
        always {
            cleanWs() // Dọn dẹp workspace sau khi chạy pipeline
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
