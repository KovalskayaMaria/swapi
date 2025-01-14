import requests
from pathlib import Path


class APIRequester:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, sw_type=''):
        try:
            responce = requests.get(self.base_url + sw_type)
            responce.raise_for_status()
            return responce
        except requests.RequestException:
            pass


class SWRequester(APIRequester):
    def __init__(self):
        super().__init__('https://swapi.dev/api/')

    def get_sw_categories(self):
        responce = self.get()
        return list(responce.json().keys())

    def get_sw_info(self, sw_type):
        return self.get(sw_type).text


def save_sw_data():
    Path('data').mkdir(exist_ok=True)
    base_url = SWRequester()
    category_list = base_url.get_sw_categories()
    for item in category_list:
        with open(f'data/{item}.txt', 'w') as file:
            file.write(base_url.get_sw_info(item))


save_sw_data()
