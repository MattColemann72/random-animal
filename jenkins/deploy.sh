#!/bin/bash

project_name=random-animal

#build-server
docker build -t ${project_name}_service-1 service-1

#build-service-2
docker build -t ${project_name}_service-2 service-2

#build-service-3
docker build -t ${project_name}_service-3 service-3

#build-service-4
docker build -t ${project_name}_service-4 service-4

#create-network
docker network create ${project_name}_network

#run-containers
docker run -d \
    -p 5000:5000 \
    --name ${project_name}_service-1 \
    --network ${project_name}_network \
    ${project_name}_service-1

docker run -d \
    -p 5000:5000 \
    --name ${project_name}_service-2 \
    --network ${project_name}_network \
    ${project_name}_service-2

docker run -d \
    -p 5000:5000 \
    --name ${project_name}_service-3 \
    --network ${project_name}_network \
    ${project_name}_service-3

docker run -d \
    -p 5000:5000 \
    --name ${project_name}_service-4 \
    --network ${project_name}_network \
    ${project_name}_service-4