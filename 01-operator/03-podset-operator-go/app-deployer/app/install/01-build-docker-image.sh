#!/usr/bin/env bash

cd ..

docker build -t gandhicloud/podset-operator-main .

docker push gandhicloud/podset-operator-main:latest
