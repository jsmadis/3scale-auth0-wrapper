
FROM python:3.7

MAINTAINER Jakub Smadiš "jakub.smadis@gmail.com"

LABEL name="threescale-auth0-wrapper"0
LABEL version="0.1"
LABEL description="A simple wrapper between 3scale and auth0"

RUN useradd -m user
WORKDIR /home/user

COPY . /threescale-auth0-wrapper/
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install pipenv
RUN venv/bin/pip install gunicorn
RUN /bin/bash -c "venv/bin/pip install -r <(venv/bin/pipenv lock -r)"
ADD . /threescale-auth0-wrapper
RUN venv/bin/pip install  /threescale-auth0-wrapper

COPY . .

RUN chmod +x startup.sh
RUN chown -R user:user ./
USER user


EXPOSE 8080
CMD ["./startup.sh"]
