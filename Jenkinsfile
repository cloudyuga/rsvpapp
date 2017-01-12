node {
   stage('build') {
       echo "build"
       git url:'https://github.com/vishalcloudyuga/rsvpapp.git
   }
   stage('test') {
       sh 'docker-compose -H 45.55.130.178:2375 up -d '
   }
   stage('staging') {
       echo "Deployed?"
       echo "check ip and port number"
       sh 'docker-compose -H 45.55.130.178:2375 ps | grep "0.0.0.0:"'
   }
   input("looks ok ?")
   stage('staging tear down') {
       sh 'docker-compose -H 45.55.130.178:2375 down'
               
   }
}
