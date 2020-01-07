# flask-on-k8s

Our app.

## Development Setup

System requirements:

```
docker
python3
docker-compose
```

Python version: we use tox to invoke our tests from multiple versions. For development you need
at least one of the python3 interpreters. Others will be skipped. CI will test the rest.

Set up a python3 virtual environment locally. We use a folder called **.env**

```
python3 -m venv .env
source .env/bin/activate
```

With your environment activated, install the development dependencies.

```
pip install tox virtualenv
pip install -r requirements.txt
pip install -r requirements_dev.txt
```

## Running the App

Running the app via `docker-compose` is a single command.

```
docker-compose up -d
```

The API can be should be testable at http://localhost:8080/api/v1/records 

Running the app locally still requires the mongo container to be running, so we
start that first and then run our local app start script.

```
docker-compose up -d mongodb
./run_local.sh
```



## Running Tests

To run unit tests locally, we use tox. This tests against installed interpreters.

```
tox
```

Unit tests can be run in a container, which has all required interpreters pre-installed.

```
# TODO fix perms
docker run -it -v $(pwd):/tmp/app -w /tmp/app --rm painless/tox /bin/bash tox
```