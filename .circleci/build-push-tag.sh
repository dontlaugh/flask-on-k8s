#!/bin/bash

REPO=quay.io/dontlaugh/flask-on-k8s
TAG=${CIRCLE_TAG}
pushd ..
docker build -t "${REPO}:${TAG}" .
popd
echo "pushing"
docker push "${REPO}:${TAG}"

