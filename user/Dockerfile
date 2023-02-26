FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update  && \
    apt-get -y --no-install-recommends install \
    build-essential \
    net-tools \
    postgresql \
    python3.9 \
    python-dev-is-python3 \
    git \
    pkg-config \
    kmod \
    cmake \
    gcc \
    ffmpeg \
    g++ \
    wget \
    python3-pip && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* ~/*

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --upgrade pip && pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app