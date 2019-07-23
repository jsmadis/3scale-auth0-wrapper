# -*- coding: utf-8 -*-

import os

from dotenv import load_dotenv

load_dotenv()


def auth0_api():
    return os.getenv('AUTH0_URL') + "/api/v2"


def auth0_oidc_config_url():
    return os.getenv('AUTH0_URL') + "/.well-known/openid-configuration"


def auth0_client_url(client_id: str):
    return auth0_api() + "/clients/" + client_id
