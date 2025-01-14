import requests
from pathlib import Path


class APIRequester:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint=''):
        try:
            responce = requests.get(self.base_url + '/' + endpoint)
            responce.raise_for_status()
            return responce
        except requests.RequestException as e:
            print(f'Ошибка подключения: {e}')
            pass


class SWRequester(APIRequester):
    def __init__(self, url='https://swapi.dev/api'):
        super().__init__(url)

    def get_sw_categories(self):
        responce = self.get()
        return list(responce.json().keys())

    def get_sw_info(self, sw_type):
        return self.get(sw_type).text


def save_sw_data():
    dir = 'data'
    Path(dir).mkdir(exist_ok=True)
    base_url = SWRequester()
    category_list = base_url.get_sw_categories()
    print(category_list)
    for item in category_list:
        with open(f'{dir}/{item}.txt', 'w') as file:
            file.write(base_url.get_sw_info(item))


if __name__ == "__main__":
    save_sw_data()
