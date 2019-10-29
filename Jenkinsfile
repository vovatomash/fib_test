pipeline {
  agent {
    node {
      label 'general-slave'
    }

  }
  stages {
    stage('Archive art') {
      steps {
        archiveArtifacts(artifacts: '*', fingerprint: true)
      }
    }
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
        stage('bo-t1 start') {
          steps {
            build(job: 'bo-t1', propagate: true, wait: true)
          }
        }
        stage('bo-t2 start') {
          steps {
            build(job: 'bo-t2', propagate: true, wait: true)
          }
        }
        stage('aaa') {
          steps {
            sh 'ls -la'
          }
        }
      }
    }
    stage('done') {
      steps {
        timestamps() {
          sh 'ls -la'
        }

      }
    }
    stage('deploy') {
      steps {
        sh 'echo "done"'
      }
    }
  }
}