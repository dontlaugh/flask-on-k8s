#!/bin/bash

minikube addons enable ingress

kubectl apply -Rf kubernetes/secrets 
kubectl create configmap db-fixture --from-file=data

helm install mongodb kubernetes/charts/mongodb
helm install app kubernetes/charts/app

