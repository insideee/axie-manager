import requests
import json
import ast
import configs


def create_account(username: str, email: str, password: str) -> dict:
    data = json.dumps({"name": username,
                       "email": email,
                       "password": password})

    request = requests.post(f'{configs.API_URL}/users', data=data)
    r_dict = ast.literal_eval(request.text)

    return {'status_code': request.status_code,
            **r_dict}


def login(email: str, password: str) -> dict:
    data = {"username": email,
            "password": password}

    request = requests.post(f'{configs.API_URL}/login', data=data)
    r_dict = ast.literal_eval(request.text)

    return {'status_code': request.status_code,
            **r_dict}
