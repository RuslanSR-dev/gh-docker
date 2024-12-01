#FROM python:3.12-alpine3.20
#
## Установка Chrome
#RUN apk update
#RUN apk add --no-cache chromium chromium-chromedriver
#
## Установка зависимостей для Chrome
#RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
#RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk
#RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk
#
## Установка Allure
#RUN apk update && \
#    apk add openjdk11-jre curl tar && \
#    curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
#    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
#    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
#    rm allure-2.13.8.tgz
#
#WORKDIR /usr/workspace
#COPY ./requirements.txt /usr/workspace
#RUN pip3 install -r requirements.txt

# Используем базовый образ, переданный как аргумент
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

# Установка Python, pip и необходимых пакетов
USER root
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv openjdk-11-jre && \
    apt-get clean

# Устанавливаем рабочую директорию
WORKDIR /usr/workspace

# Копируем requirements.txt для установки зависимостей
COPY ./requirements.txt /usr/workspace

# Устанавливаем зависимости
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt --break-system-packages
#    pip3 install -r requirements.txt || pip3 install -r requirements.txt --break-system-packages