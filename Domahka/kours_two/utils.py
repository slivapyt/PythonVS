import requests
# import json
from random import choice


def load_web_dictionary():
    '''Получаем данные о студенте из json'''
    web_words = "https://www.jsonkeeper.com/b/ETPW"
    web_4len = requests.get(web_words)
    data = web_4len.json()
    return choice(data)
