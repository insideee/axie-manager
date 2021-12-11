import requests
import json
import ast

API_URL = 'http://127.0.0.1:8000'

def create_account(username: str, email: str, password: str):
    data = json.dumps({"name": username,
            "email": email,
            "password": password})
    
    request = requests.post(f'{API_URL}/users', data=data)
    r_dict = ast.literal_eval(request.text)
    
    return {'status_code': request.status_code,
            **r_dict}
    

if __name__ == '__main__':
    a = create_account(username='mariaa', email='jas@g.c', password='hoje')
    
    print(a)
    
    
