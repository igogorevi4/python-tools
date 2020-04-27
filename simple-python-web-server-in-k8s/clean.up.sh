#!/usr/bin/env bash

KUBECTL=$(which kubectl)
DOCKER=$(which docker)

cd k8s/
echo "========= Cleaning up the kubernetes..."
$KUBECTL delete -f ingress.yaml && \
    $KUBECTL delete -f app.yaml && \
    $KUBECTL delete -f cloud-generic.yaml && \
    $KUBECTL delete -f mandatory.yaml && \
    echo "========= Cluster has been deleted successfully."

echo "========= Removing a docker image of a simple python-web-server"
$DOCKER rmi $(docker images | grep simple-python-app | awk '{print $3}')
