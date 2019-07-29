FROM ubuntu:18.04
FROM python:3.7

MAINTAINER Jakub Smadiš "jakub.smadis@gmail.com"

LABEL name="threescale-auth0-wrapper"0
LABEL version="0.1"
LABEL description="A simple wrapper between 3scale and auth0"

RUN useradd -m user
USER user

ENV PATH="/home/user/.local/bin:${PATH}"

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ADD Pipfile Pipfile.lock /threescale-auth0-wrapper/
RUN pip install --user --no-cache-dir pipenv
COPY . /threescale-auth0-wrapper/

ADD Pipfile Pipfile.lock /threescale-auth0-wrapper/
WORKDIR /threescale-auth0-wrapper
RUN /bin/bash -c "pip install --user -r <(pipenv lock -r)"

ADD . /threescale-auth0-wrapper
RUN pip install --user /threescale-auth0-wrapper

EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "threescale-auth0-wrapper:app", "-k", "gevent"]