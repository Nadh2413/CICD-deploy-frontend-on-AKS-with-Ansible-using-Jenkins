pineline {
  agent any
stages {
        stage('Hello') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-user', url: 'https://github.com/Nadh2413/cafe-app.git']])
                sh 'pwd'
                sh 'ls'
                sh 'python3 /projects/aler_telegram.py'
            }
        }
    }

  
}
