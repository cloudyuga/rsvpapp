stage('test') {
node ('docker-jenkins-slave'){
  git "${gitrepo}"
  sh 'chmod a+x ./run_test.sh'
  sh './run_test.sh'
}
}

node() {
git "${gitrepo}"
stage('build the image') {
  withDockerServer([credentialsId: 'dockerhost', uri: "tcp://${dockerhosturl}:2376"]) {
    docker.build "${dockerhub}/rsvpapp:mooc"
  }
}
stage('push the image to DockerHub') {
withDockerServer([credentialsId: 'dockerhost', uri: "tcp://${dockerhosturl}:2376"]) {
  withDockerRegistry([credentialsId: 'dockerhub_auth']) {
    docker.image("${dockerhub}/rsvpapp:mooc").push()
   }
}        
}
stage('deploy the image to staging server') {
        withDockerServer([credentialsId: 'staging-server', uri: "tcp://${stagingurl}:2376"]){
          sh 'docker-compose pull'
          sh 'docker-compose -p rsvp_staging up -d'
        }
        input "Check application running at http://${stagingurl}:5000 looking good?"
        withDockerServer([credentialsId: 'staging-server', uri: "tcp://${stagingurl}:2376"]) {
          sh 'docker-compose -p rsvp_staging down -v'
        }
   }  
  
   stage('deploy in production'){
   withDockerServer([credentialsId: 'production', uri: "tcp://${productionurl}:2376"]) {

          sh 'docker stack deploy -c docker-stack.yaml myrsvpapp'

          }
   input "Check application running at http://${productionurl}:5000"
   withDockerServer([credentialsId: 'production', uri: "tcp://${productionurl}:2376"]) {

            sh 'docker stack down myrsvpapp'

      }

   } 
   
}
