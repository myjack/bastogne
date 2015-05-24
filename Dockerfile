FROM ubuntu:15.04
MAINTAINER imaguowei@gmail.com

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y build-essential
RUN apt-get install -y git
RUN apt-get install -y wget
RUN apt-get install -y vim

RUN apt-get install -y python3.4
RUN apt-get install -y python3.4-dev

WORKDIR /tmp

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

RUN apt-get install -y zsh
RUN wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O - | sh

RUN apt-get install nginx
EXPOSE 80


ENTRYPOINT service nginx start