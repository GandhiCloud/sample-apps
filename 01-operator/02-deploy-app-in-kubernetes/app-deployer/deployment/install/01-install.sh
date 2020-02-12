#!/usr/bin/env bash

echo 'installation started .............................'

cd ../src

oc apply -f 01-namespace.yaml
oc apply -f 11-crd.yml
oc apply -f 12-role.yml
oc apply -f 21-operator.yml
oc apply -f 31-application-wcare-mutual.yaml.yml

echo 'installation completed .............................'
