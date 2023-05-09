import psycopg2
import requests

from bs4 import BeautifulSoup

import datetime

host = 'localhost'
port = '5432'
database = 'database'
user = 'postgres'
password = '8228337lolWAT'

conn = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)

cursor = conn.cursor()


cursor.execute(sql, data)

conn.commit()

conn.close()