#!/bin/bash

REPO=quay.io/dontlaugh/flask-on-k8s
COMMIT=$(git rev-parse --short HEAD)
TAG=${COMMIT}-${CIRCLE_BUILD_NUM}
pushd ..
docker build -t "${REPO}:${TAG}" .
popd
echo "pushing"
docker push "${REPO}:${TAG}"
