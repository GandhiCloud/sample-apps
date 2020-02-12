FROM python:latest
RUN pip install requests
RUN pip install pyyaml
RUN pip install kubernetes
WORKDIR /app

COPY ./src /app

RUN ls -la /app
RUN chmod -R 777 /app

ENTRYPOINT [ "python", "/app/main.py" ]