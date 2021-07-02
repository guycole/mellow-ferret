#
# ferret development environment
#
# docker build . -t ferret-dev
#
# docker run --rm -it -v ~/documents/github:/home/gsc/github ferret-dev /bin/bash
#
FROM ubuntu:18.04
LABEL build_date="2021-07-01"
LABEL description="ferret development"
LABEL maintainer="guycole@gmail.com"
#
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y
#
#RUN apt-get install -y python3 
#RUN apt-get install -y python3-pip 
#RUN apt-get install -y virtualenv
#RUN pip3 install --upgrade pip
#
RUN apt-get install -y curl
RUN apt-get install -y git 
RUN apt-get install -y less
#RUN apt-get install -y inetutils-tools inetutils-ping inetutils-telnet
#RUN apt-get install -y netcat
#RUN apt-get install -y net-tools
RUN apt-get install -y vim
RUN apt-get install -y wget
#
RUN apt-get install -y cmake
RUN apt-get install -y build-essential
RUN apt-get install -y libusb-1.0-0-dev
#RUN apt-get install -y postgresql-client
#
RUN apt-cache pkgnames | sort > pkg.names
#
RUN useradd -m -s /bin/bash gsc 
COPY bash_aliases /home/gsc/.bash_aliases
RUN mkdir /home/gsc/github
#
