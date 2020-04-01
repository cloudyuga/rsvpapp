pipeline {
    agent {
      kubernetes  {
            label 'jenkins-slave'
        }
    }
 
  stages {

    stage('Build') {
      environment {
        DOCKERHUB_CREDS = credentials('dockerhub')
        IMAGE_REPO = "atul7cloudyuga/rsvp-demo"
      }
      steps {
        container('docker') {
          // Build new image
          sh "until docker ps; do sleep 3; done && docker build -t atul7cloudyuga/rsvp-demo:${env.GIT_COMMIT} ."
          // Publish new image
          sh "docker login --username $DOCKERHUB_CREDS_USR --password $DOCKERHUB_CREDS_PSW && docker push ${env.IMAGE_REPO}:${env.GIT_COMMIT}"
        }
      }
    }

    stage('Deploy E2E') {
      environment {
        GIT_CREDS = credentials('github')
        GIT_REPO_URL = "github.com/atul7cloudyuga/kustomize-demo.git"
        GIT_REPO_EMAIL = 'atul@cloudyuga.guru'
        GIT_REPO_BRANCH = "9-putting-it-all-together-fixing-labels"
        IMAGE_REPO = "atul7cloudyuga/rsvp-demo"
        
      }
      steps {
        container('tools') {
            sh "git clone https://$GIT_CREDS_USR:$GIT_CREDS_PSW@${env.GIT_REPO_URL}"
            sh "git config --global user.email ${env.GIT_REPO_EMAIL}"

          dir("kustomize-demo") {
              sh "git checkout ${env.GIT_REPO_BRANCH}"
              sh "cd ./overlays/staging && kustomize edit set image ${env.IMAGE_REPO}:${env.GIT_COMMIT}"
            sh "git commit -am 'Publish new version' && git push || echo 'no changes'"
          }
        }
      }
    }

    stage('Deploy to Prod') {
        environment {
        IMAGE_REPO = "atul7cloudyuga/rsvp-demo"
      }
      steps {
        input message:'Approve deployment?'
        container('tools') {
          dir("kustomize-demo") {
              sh "cd ./overlays/prod && kustomize edit set image ${env.IMAGE_REPO}:${env.GIT_COMMIT}"
            sh "git commit -am 'Publish new version' && git push || echo 'no changes'"
          }
        }
      }
    }
  }
}
