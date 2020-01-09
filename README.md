# flask-on-k8s

A demo flask app with CI/CD, unit tests, and a local Kubernetes deployment.

## Development Setup

We use tox to invoke our tests from multiple versions. For development you need
at least one python3 interpreter. See tox.ini for the supported versions.

Set up a python3 virtual environment locally. We use a folder called **.env**

```
virtualenv -p python3 .venv
source .venv/bin/activate
```

With your environment activated, install the development dependencies.

```
pip install tox 
pip install -r requirements.txt
pip install -r requirements_dev.txt
```

## Running the App: docker-compose

Running the app via `docker-compose` is a single command.

```
docker-compose up -d
```

The API can be should be testable at http://localhost:8080/api/v1/records 

## Building the App: docker-compose

Rebuild the container on demand with docker-compose.

```
docker-compose build app
```

## Running the App: local

Running the app locally still requires the mongo container to be running, so we
start that first with docker-compose. Then we run our local app start script.

```
docker-compose up -d mongodb
./tools/run-local.sh
```

## Running Tests

To run unit tests locally, we use tox. This tests against installed interpreters.
Others will be skipped. CI will test the rest.

```
tox
```

## CircleCI

Tests on CircleCI should run in a tox container on every git push.

[The CircleCI project is here](https://circleci.com/gh/dontlaugh/flask-on-k8s)

If tests pass, a container is pushed to the Quay.io registry on every git push.

[The Quay.io container registry is here](https://quay.io/repository/dontlaugh/flask-on-k8s?tab=tags)

## Releases

Releases are git tags with a semver structure.

Releases run through the **tag-release** workflow on CircleCI, which also runs 
tests. In the release workflow, the final container has the semver tag instead 
of a raw git hash + build number..

Release by pushing a tag to GitHub.

```
git tag v0.1.0
git push --tags
```

Then wait for tests to pass. Your container will be pushed to Quay.

## Kubernetes Deployment

We have a local kubernetes setup which requires the following components:

* [minikube 1.6.2](https://kubernetes.io/docs/tasks/tools/install-minikube/)
* [helm 3](https://helm.sh/docs/intro/install/)
* [kubectl 1.17.0](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-linux)

Other minikube and kubectl versions may work, but helm 3 is required.


Start minikube and enable ingress

```
minikube start
minikube addons enable ingress
```

Load secrets and config maps

```
kubectl apply -Rf kubernetes/secrets
kubectl create configmap db-fixture --from-file=data
```

deploy with helm

```
helm install mongodb kubernetes/charts/mongodb
helm install app kubernetes/charts/app
```

Expose the service to your host for testing

```
kubectl expose deployment app-deployment --target-port 8080 --type NodePort
```

Test the exposed port with curl (and jq, if you have it)

```
curl $(minikube service app --url)/api/v1/records | jq
```

## Updating the Kubernetes Deployment

Once a new container build has made it to Quay, we can update the `tag` value
in our app's helm values file **kubernetes/charts/app/values.yaml**. Then we can 
upgrade.

```
helm upgrade app kubernetes/charts/app
```

## Kubernetes Troubleshooting

Test mongo connectivity (via kube DNS) in an ad hoc shell with `kubectl run`

```
kubectl run dnstest -it --image=fedora --rm -- /bin/bash
dnf install -y dnsutils wget
wget https://repo.mongodb.org/yum/redhat/8/mongodb-org/4.2/x86_64/RPMS/mongodb-org-shell-4.2.2-1.el8.x86_64.rpm
rpm -i mongodb-org-shell-4.2.2-1.el8.x86_64.rpm 
mongo 'mongodb://testuser:testpassword!@mongodb/db'
```

Once in a mongo shell, switch to our test fixture and query for all records to
ensure our database fixture has loaded.

```
> use db
> db.record.find({})
```
