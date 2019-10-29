pipeline {
  agent {
    node {
      label 'general-slave'
    }

  }
  stages {
    stage('error') {
      parallel {
        stage('test1') {
          steps {
            echo 'aaa'
          }
        }
        stage('test2') {
          steps {
            sleep 3
            echo 'sleep'
          }
        }
      }
    }
    stage('done') {
      steps {
        sh 'ls -la'
      }
    }
  }
}