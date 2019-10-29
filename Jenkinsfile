pipeline {
  agent {
    node {
      label 'general-slave'
    }

  }
  stages {
    stage('test1') {
      parallel {
        stage('test1') {
          steps {
            sh 'sh "python3 ./fibo.py --count 2"'
          }
        }
        stage('test2') {
          steps {
            sh 'sh "python3 ./fibo.py --count 4"'
          }
        }
        stage('test3') {
          steps {
            sh 'sh "python3 ./fibo.py --count 5"'
          }
        }
        stage('run bo-t1') {
          steps {
            build(job: 'bo-t1', propagate: true, wait: true)
          }
        }
        stage('run bo-t2') {
          steps {
            build(job: 'bo-t2', propagate: true, wait: true)
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