# -*- coding: utf-8 -*-

import requests

from flask import Flask, request, make_response
from .config import auth0_client_url, auth0_oidc_config_url
from .auth0.client import threescale_format, auth0_format

app = Flask(__name__)


@app.route("/.well-known/openid-configuration", methods=["GET"])
def oidc_config():
    response = requests.get(auth0_oidc_config_url())
    return response.content


@app.route("/clients/<path:client_id>", methods=["GET"])
def client_get(client_id: str):
    headers = request.headers
    response = requests.get(auth0_client_url(client_id), headers=headers)
    return make_response(threescale_format(response.content), response.status_code)


@app.route("/clients/<path:client_id>", methods=["PUT"])
def client_put(client_id: str):
    headers = request.headers
    payload = auth0_format(request.get_json())
    if check_client_existence(client_id, headers):
        response = requests.patch(auth0_client_url(client_id), data=payload, headers=headers)
    else:
        response = requests.post(auth0_client_url(client_id), data=payload, headers=headers)
    return make_response(threescale_format(response.content), response.status_code)


@app.route("/clients/<path:client_id>", methods=["DELETE"])
def client_delete(client_id: str):
    headers = request.headers
    response = requests.delete(auth0_client_url(client_id), headers=headers)
    return make_response(threescale_format(response.content), response.status_code)


def check_client_existence(client_id: str, headers: dict):
    response = requests.get(auth0_client_url(client_id), headers=headers)
    return response.status_code == 200


if __name__ == "__main__":
    app.run(debug=True)
