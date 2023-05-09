import psycopg2
import requests

from bs4 import BeautifulSoup

import classes.DataTransform

"""from dataSave import region, tnved, stoim, netto, kol, period, nastranapr, napr"""

from config import host, user, password, db_name, port
import datetime

"""classes.DataExtract.stealData()"""
classes.DataTransform.Extraction()

"""try:
    connection = psycopg2.connect(
        port=port,
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    with connection.cursor() as cursor:
        sql = "INSERT INTO database.customs_data (region_id, tnved_id, unit_id, stoim, netto, kol, year_id, list_countries_id, month_id, export) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        data = (1, '0101', 3, 55, 55, 55, 1897, '1B', 12, True)
        cursor.execute(sql, data)
        connection.commit()

except Exception as _ex:
    print("[Info] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")"""

