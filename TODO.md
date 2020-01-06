

* tox should run locally
* tox should run on CI natively
* docker compose is the default way to run (we do a build)
* we build via compose
* subcommand - push our container (how to specify flask version)
* use class for flask http response
* document setting up virtualenv

Create gunicorn entry script
example: https://github.com/testdrivenio/flask-vue-kubernetes/blob/master/services/server/entrypoint.sh

## kubernetes
* helm chart k8s
* docs: k8s deployment procedure
* flask health endpoint - check db conn
* mongodb endpoint - process check
* mongodb persistent volume?
* kubernetes post-deploy hook for setting up database


