FROM python:latest
RUN pip install requests
WORKDIR /app

COPY ./src /app

RUN ls -la /app

ENTRYPOINT [ "python", "/app/main.py" ]