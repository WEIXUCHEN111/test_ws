pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'git@github.com:WEIXUCHEN111/test_ws.git'
            }
        }

        stage('Build C++') {
            steps {
                dir('src/cpp_demo') {
                    sh 'g++ main.cpp -o main'
                }
            }
        }

        stage('Run Test Script') {
            steps {
                sh 'python3 src/test.py'
            }
        }
    }
}

