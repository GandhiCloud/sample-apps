#!/usr/bin/env bash
echo 'deploy process started .............................'

ls -la /app-files/
cp /app-files/* /html

echo 'after copyy .........'
ls -la /app-files/
ls -la /html

echo 'deploy process completed .............................'