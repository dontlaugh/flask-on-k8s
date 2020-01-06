#!/bin/bash

#docker run --net=host --name mdb --rm \
#    -e MONGO_INITDB_ROOT_USERNAME=mongoadmin \
#    -e MONGO_INITDB_ROOT_PASSWORD=secret \
#    mongo --noauth

docker run --net=host --name mdb --rm \
    mongo --noauth

