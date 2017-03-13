stage('test') {
node ('docker-jenkins-slave'){
  git 'https://github.com/vishalcloudyuga/rsvpapp.git'
  sh 'chmod a+x ./run_test.sh'
  sh './run_test.sh'
}
}

node() {
git 'https://github.com/vishalcloudyuga/rsvpapp.git'
stage('build the image') {
  withDockerServer([credentialsId: 'dockerhost', uri: "tcp://${dockerhosturl}:2376"]) {
    docker.build 'coolvbgarya/rsvpapp:mooc'
  }
}
stage('push the image to DockerHub') {
withDockerServer([credentialsId: 'dockerhost', uri: "tcp://${dockerhosturl}:2376"]) {
  withDockerRegistry([credentialsId: 'dockerhub_auth']) {
    docker.image('coolvbgarya/rsvpapp:mooc').push()
   }
}        
}
stage('deploy the image to staging server') {
        withDockerServer([credentialsId: 'staging-server', uri: "tcp://${stagingurl}:2376"]){ 
          sh 'docker-compose -p rsvp_staging up -d'
        }
        input "Check application running at http://${stagingurl}:5000 looking good?"
        withDockerServer([credentialsId: 'staging-server', uri: "tcp://${stagingurl}:2376"]) {
          sh 'docker-compose -p rsvp_staging down -v'
        }
   }   
   
}
