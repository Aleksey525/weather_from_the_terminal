import requests


params = {'lang': 'ru', 'T': '', 'm': '', 'M': '', 'n': '', 'q': ''}
cities = ['Лондон', 'Шереметьево', 'Череповец']
url_template = 'https://wttr.in/{}?'


def get(u: str, p: dict) -> str:
    response = requests.get(u, params=p)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    for i in cities:
        url = url_template.format(i)
        print(get(url, params))
