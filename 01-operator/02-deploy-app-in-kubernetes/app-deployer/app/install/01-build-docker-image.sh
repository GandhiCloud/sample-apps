#!/usr/bin/env bash

cd ..

docker build -t gandhicloud/g-appdeploy-operator .

docker push gandhicloud/g-appdeploy-operator:latest
