

minikube addons enable ingress

kk apply -Rf kubernetes/secrets 
kk create configmap db-fixture --from-file=data

helm3 install mongodb kubernetes/charts/mongodb
helm3 install app kubernetes/charts/app

