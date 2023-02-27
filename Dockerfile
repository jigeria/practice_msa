FROM python:3.11

ARG DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --upgrade pip && pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app