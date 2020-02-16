#!/usr/bin/env bash

KUBECTL=$(which kubectl)
DOCKER=$(which docker)

echo "========= Building an image of a simple python-web-server"
$DOCKER build -t simple-python-app .

cd k8s/
echo "========= Creating simple web-cluster in kubernetes..."
$KUBECTL apply -f mandatory.yaml && \
    $KUBECTL apply -f cloud-generic.yaml && \
    $KUBECTL apply -f app.yaml && \
    $KUBECTL apply -f ingress.yaml && \
    echo "========= Cluster has been started successfully."
