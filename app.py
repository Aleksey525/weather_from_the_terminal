import requests


params = {'lang': 'ru', 'T': '', 'm': '', 'M': '', 'n': '', 'q': ''}
cities = ['Лондон', 'Шереметьево', 'Череповец']
url_template = 'https://wttr.in/{}?'


def get_response_text(url_complite: str, user_params: dict) -> str:
    response = requests.get(url_complite, params=user_params)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    for city in cities:
        url = url_template.format(city)
        print(get_response_text(url, params))
