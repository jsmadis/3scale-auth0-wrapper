import json


def threescale_format(json_data: str):
    json_data = json.loads(json_data)
    data = {
        "client_id": json_data['client_id'],
        "client_secret": json_data['client_secret'],
        "grant_types": json_data['grant_types'],
        "client_name": json_data['name'],
        "redirect_uris": json_data['callbacks']
    }
    return json.dumps(data)


def auth0_format(json_data: str):
    json_data = json.loads(json_data)
    data = {
        "client_id": json_data['client_id'],
        "client_secret": json_data['client_secret'],
        "grant_types": json_data['grant_types'],
        "name": json_data['client_name'],
        "callbacks": json_data['redirect_uris']
    }
    return json.dumps(data)


def threescale_token_format(json_data: str):
    json_data = json.loads(json_data)
    return json.dumps({"token_endpoint": json_data['token_endpoint']})
