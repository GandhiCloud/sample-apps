#!/usr/bin/env bash

echo 'un-installation started .............................'

cd ../src

oc delete -f 31-application-wcare-mutual.yaml.yml
oc delete -f 21-operator.yml
oc delete -f 12-role.yml
oc delete -f 11-crd.yml
oc delete -f 01-namespace.yaml

echo 'un-installation completed .............................'
