pipeline {
    agent any
    environment {
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
    }
    stages {
        stage('Install Requirements') {
            steps {
                sh 'bash jenkins/install-requirements.sh'
            }
        }
        stage('Test') {
            steps {
                //pytest
                //run for each service
                //produce cov reports
                sh 'bash jenkins/test.sh'
            }
        }
        stage('Build') {
            steps {
                // install docker and docker compose
                //docker-compose build
                sh 'docker system prune --force --all'
                sh 'docker-compose build --parallel'
            }
        }
        stage('Push') {
            steps {
                // install docker and docker compose
                //docker-compose push
                sh 'docker-compose push'
            }
        }
        stage('Config Management - Ansible') {
            steps {
                //install ansible on jenkins machine for jenkins user
                //ansible-playbook -i inventory.yaml playbook.yaml
                sh 'cd ansible && ansible-playbook -i inventory.yaml playbook.yaml'
            }
        }
        stage('Deploy') {
            steps {
                // create swarm infrastructure
                // copy over docker-compose.yaml
                // ssh: docker stack deploy --compose-file docker-compose.yaml animals
                sh 'echo deploy'
            }
        }
    }
}