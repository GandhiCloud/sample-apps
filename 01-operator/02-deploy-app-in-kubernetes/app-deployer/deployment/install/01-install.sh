#!/usr/bin/env bash

echo 'installation started .............................'

cd ../src

oc apply -f 01-namespace.yaml
oc apply -f 11-crd.yaml
oc apply -f 12-serviceaccount-role.yaml
oc apply -f 21-operator.yaml
oc apply -f 31-application-wcare-mutual.yaml

echo 'installation completed .............................'
