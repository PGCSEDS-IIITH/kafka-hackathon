FROM python:3.8-slim
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV DISPLAY=:99

# Install apt requirements
RUN apt update
RUN apt install -y wbritish

# Install requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app
