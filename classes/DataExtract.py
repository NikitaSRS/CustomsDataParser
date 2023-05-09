import requests
"""import fake_useragent"""
from bs4 import BeautifulSoup


def stealData():
    link = "http://stat.customs.gov.ru/unload"

    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lmxl')
    block = soup.find('div', class_  = 'Wrapper__wrapper wrapper_theme_default')
    typeBoxes = block.find('div', class_ = 'UnloadForm__line')

    print(typeBoxes)