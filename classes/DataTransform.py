import requests
"""import fake_useragent"""
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

def Extraction():

    archive = 'DataContainer/DATTSVT.csv.zip'

    zip_file =ZipFile(archive)

    [text_file.filename for text_file in zip_file.infolist() ]


    zipfile = 'DataContainer/DATTSVT.csv.zip'

    z = ZipFile(zipfile)

    return z.infolist()