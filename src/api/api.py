""" Thanks to jchbasco for the free api on rapidapi
    link: https://rapidapi.com/jchbasco/api/axie-infinity/
"""

import requests
import ast

class FullData:

    def __init__(self, ronin_address: str) -> None:

        self.url = 'https://axie-infinity.p.rapidapi.com/get-final-data/'

        self.querystring = {'id':f'{ronin_address}'}

        self.headers = {
            'x-rapidapi-host': 'axie-infinity.p.rapidapi.com',
            'x-rapidapi-key': '2176b88cb0mshdce0dc19064eacap1c5344jsna2e5d5806e1f'
            }

        self.response = requests.request('GET', self.url+self.querystring['id'], headers=self.headers, params=self.querystring)

        self.data = ast.literal_eval(self.response.text)

class DailySlp:

    def __init__(self, ronin_address: str) -> None:

        self.url = f'https://axie-infinity.p.rapidapi.com/get-daily/{ronin_address}'

        self.headers = {
            'x-rapidapi-host': 'axie-infinity.p.rapidapi.com',
            'x-rapidapi-key': '2176b88cb0mshdce0dc19064eacap1c5344jsna2e5d5806e1f'
            }

        self.response = requests.request('GET', self.url, headers=self.headers)

        self.data = ast.literal_eval(self.response.text)

class AccAxie:

    def __init__(self, ronin_address: str) -> None:

        self.url = f'https://axie-infinity.p.rapidapi.com/get-axies/{ronin_address}'

        self.headers = {
            'x-rapidapi-host': 'axie-infinity.p.rapidapi.com',
            'x-rapidapi-key': '2176b88cb0mshdce0dc19064eacap1c5344jsna2e5d5806e1f'
            }

        self.response = requests.request('GET', self.url, headers=self.headers)

        self.data = ast.literal_eval(self.response.text)
