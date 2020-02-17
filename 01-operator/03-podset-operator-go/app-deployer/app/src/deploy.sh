#!/usr/bin/env bash

echo 'deploy process started .............................'

sed -i "" 's|__NAMESPACE__|$NAMESPACE|g' ./kube-resources/*.yaml
sed -i "" 's|__APP_NAME__|$APP_NAME|g' ./kube-resources/*.yaml
sed -i "" 's|__CONTAINER_PORT__|$CONTAINER_PORT|g' ./kube-resources/*.yaml
sed -i "" 's|__IMAGE_NAME__|$IMAGE_NAME|g' ./kube-resources/*.yaml
sed -i "" 's|__IMAGE_TAG__|$IMAGE_TAG|g' ./kube-resources/*.yaml

cat ./kube-resources/01-namespace.yaml
cat ./kube-resources/02-deployment.yaml
cat ./kube-resources/03-service.yaml
cat ./kube-resources/04-route.yaml


echo 'deploy process completed .............................'