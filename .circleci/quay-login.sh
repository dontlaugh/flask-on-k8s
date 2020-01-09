#!/bin/bash

# These secrets are provided in CircleCI's backend
docker login -u ${QUAY_USERNAME} -p ${QUAY_PASSWORD} quay.io
