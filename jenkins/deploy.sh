#!/bin/bash

#copy over compose.yaml to manager node
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@10.154.0.24:home/jenkins/docker-compose.yaml

#docekr stack deploy
ssh -i ~/.ssh/ansible_id_rsa jenkins@10.154.0.24 << EOF
    export DATABASE_URI=${DATABASE_URI}
    docker stack deploy --compose-file docker-compose.yaml random-animal
EOF
