docker pull jenkins/jenkins:lts
ls -nd /home/jenkins
chown -R 1000:1000 /home/jenkins
docker run -itd -p 9090:8080 -p 50000:50000 --name jenkins --privileged=true -b /home/jenkins:/var/jenkins_home jenkins/jenkins:lts