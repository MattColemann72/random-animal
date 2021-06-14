#!/bin/bash

#copy over compose.yaml to manager node
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@10.154.0.29:/home/jenkins/docker-compose.yaml

#docekr stack deploy
ssh -i ~/.ssh/ansible_id_rsa jenkins@10.154.0.29 << EOF
    export DATABASE_URI=${DATABASE_URI}
    export DOCKER_USERNAME=${DOCKER_USERNAME}
    export DOCKER_PASSWORD=${DOCKER_PASSWORD}
    docker stack deploy --compose-file docker-compose.yaml random-animal
EOF
