FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3

COPY * /opt/

WORKDIR /opt

CMD ["python3", "main.py"]

