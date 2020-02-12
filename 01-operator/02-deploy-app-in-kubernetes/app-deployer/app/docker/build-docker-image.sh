#!/usr/bin/env bash

cd ..

docker build -f docker/Dockerfile -t gandhicloud/g-appdeploy-operator .

docker push gandhicloud/g-appdeploy-operator:latest
