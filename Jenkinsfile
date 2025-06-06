pipeline {
    agent any

    stages {
        stage('Build C++') {
            steps {
                sh 'g++ src/cpp_demo/main.cpp -o src/cpp_demo/main'
            }
        }

        stage('Run Test Script') {
            steps {
                sh 'python3 src/test.py'
            }
        }
    }
}

