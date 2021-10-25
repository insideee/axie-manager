""" Thanks to jchbasco for the free api on rapidapi
    link: https://rapidapi.com/jchbasco/api/axie-infinity/
"""

import requests
import ast
import json
from datetime import datetime


class FullData:

    def __init__(self, ronin_address: str) -> None:

        self.url = 'https://axie-infinity.p.rapidapi.com/get-update'

        self.querystring = {'id': f'0x{ronin_address}'}
        self.ronin_acc = self.querystring['id']

        self.headers = {
            'x-rapidapi-host': 'axie-infinity.p.rapidapi.com',
            'x-rapidapi-key': '2176b88cb0mshdce0dc19064eacap1c5344jsna2e5d5806e1f'
        }

        self.response = requests.request('GET', self.url + f'/{self.ronin_acc}', headers=self.headers,
                                         params=self.querystring)

        response_treated = self._response_treatment()
        
        self.data = ast.literal_eval(response_treated)

    def _response_treatment(self) -> str:
        replace_dict = {'null': '"null"',
                        'false': '"false"'}

        response_str = self.response.text

        for k, v in replace_dict.items():
            response_str = response_str.replace(k, v)

        return response_str

    def get_daily_slp(self) -> int:
        for k, v in self.data.items():
            if k == 'slp':
                if self.data['slp']['todaySoFar'] == 'null':
                    return 0
                    
                return self.data['slp']['todaySoFar']

    def get_yesterday_slp(self) -> int:
        for k, v in self.data.items():
            if k == 'slp':
                if self.data['slp']['yesterdaySLP'] == 'null':
                    return 0

                return self.data['slp']['yesterdaySLP']

    def get_account_slp(self) -> int:
        for k, v in self.data.items():
            if k == 'slp':
                return self.data['slp']['total']

    def get_average_slp(self) -> int:
        for k, v in self.data.items():
            if k == 'slp':
                if self.data['slp']['average'] == 'null':
                    return 0

                return self.data['slp']['average']

    def get_mmr(self):
        for k, v in self.data.items():
            if k == 'leaderboard':
                return self.data['leaderboard']['elo']

    def get_rank(self):
        for k, v in self.data.items():
            if k == 'leaderboard':
                return self.data['leaderboard']['rank']

class AccAxie:

    def __init__(self, ronin_address: str) -> None:

        self.url = f'https://axie-infinity.p.rapidapi.com/get-axies/0x{ronin_address}'

        self.headers = {
            'x-rapidapi-host': 'axie-infinity.p.rapidapi.com',
            'x-rapidapi-key': '2176b88cb0mshdce0dc19064eacap1c5344jsna2e5d5806e1f'
        }

        self.response = requests.request('GET', self.url, headers=self.headers)
        self.response_str = self._response_treatment()

        self.data = ast.literal_eval(self.response_str)

    def _response_treatment(self) -> str:
        replace_dict = {'null': '"null"',
                        'false': '"false"'}

        response_str = self.response.text

        for k, v in replace_dict.items():
            response_str = response_str.replace(k, v)

        return response_str

    def get_axie_data_str(self) -> str:
        try:
            list_axies = self.data['data']['axies']['results']
            dict_axies = {}

            for i in range(0, len(list_axies)):
                dict_axies[f'{i}'] = list_axies[i]
        except Exception:
            dict_axies = {}

        return json.dumps(dict_axies)

    def get_axie_data_dict(self) -> dict:
        list_axies = self.data['data']['axies']['results']
        dict_axies = {}

        for i in range(0, len(list_axies)):
            dict_axies[f'{i}'] = list_axies[i]

        return dict_axies


if __name__ == '__main__':
    # a = AccAxie('7bad5c65f2e2c53e65a5c32d330c070c337ce066')
    # str_a = a.get_axie_data_str()
    # dict_a = a.get_axie_data_dict()
    # print(type(dict_a), type(str_a), len(dict_a))

    #a = FullData('523a6ca8c09f0653f8b69ce09d3f3d1d2f714101')
    # daily = a.get_daily_slp()

    time_now = datetime.now()
    formated_datetime = time_now.strftime('%Y-%m-%d %H:%M')

    print(formated_datetime, type(formated_datetime))
