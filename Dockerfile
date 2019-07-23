FROM ubuntu:18.04
FROM python:3.7

MAINTAINER Jakub Smadiš "jakub.smadis@gmail.com"

LABEL name="3scale-auth0-wrapper"0
LABEL version="0.1"
LABEL description="A simple wrapper between 3scale and auth0"


ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ADD Pipfile Pipfile.lock /httpbin/
RUN pip3 install --no-cache-dir pipenv
COPY . /3scale-auth0-wrapper/

ADD Pipfile Pipfile.lock /3scale-auth0-wrapper/
WORKDIR /3scale-auth0-wrapper

RUN pip3 install --no-cache-dir /3scale-auth0-wrapper

EXPOSE 80

ENTRYPOINT ["python3.7"]
CMD ["3scale-auth0-wrapper/core.py"]