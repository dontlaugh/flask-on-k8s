#!/bin/bash

REPO=quay.io/dontlaugh/flask-on-k8s
TAG=${CIRCLE_TAG}
docker build -t "${REPO}:${TAG}" .
docker push "${REPO}:${TAG}"
