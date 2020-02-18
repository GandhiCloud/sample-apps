#Download base image ubuntu 16.04
FROM ubuntu:16.04
 
# Update Software repository
RUN apt-get update

WORKDIR /app-files
COPY ./src /app-files

RUN ls -la /app-files
RUN chmod -R 777 /app-files

# VOLUME /app-files

ENTRYPOINT [ "/app-files/main.sh" ]