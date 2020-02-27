#!/usr/bin/env bash

cd ..

docker build -t gandhicloud/greetings-operator-main .

docker push gandhicloud/greetings-operator-main:latest
