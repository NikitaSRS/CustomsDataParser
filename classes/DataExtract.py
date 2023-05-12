import zipfile
import csv
import os
import psycopg2

from config import host, user, password, db_name, port

month_nd_days = {
    '01': "31",
    '03': "31",
    '04': "30",
    '05': "31",
    '06': "30",
    '07': "31",
    '08': "31",
    '09': "30",
    '10': "31",
    '11': "30",
    '12': "31"
}

def main():
    year = checkYear()
    month = checkMonth()
    if len(str(month)) == 1:
        monthS = "0" + str(month)
    else:
        monthS = str(month)
    start_date = str(year) + "-" + monthS + "-" + (leapYear(year) if month == 2 else str(month_nd_days[monthS]))
    if monthS == "12":
        monthS = "01"
        year += 1
    else:
        monthS = "0" + str(month + 1) if len(str(month)) == 1 else str(month + 1)
    end_date = str(year) + "-" + monthS + "-" + (leapYear(year) if month + 1 == 2 else str(month_nd_days[monthS]))
    print(start_date, end_date)
    ExtractDataFromCustoms(start_date, end_date)
def ExtractDataFromCustoms(start_pos, end_pos):
    return 0
def leapYear(year):
    if year % 4 == 0:
        return "29"
    else:
        return "28"
def checkYear():
    try:
        connection = psycopg2.connect(
            port=port,
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        with connection.cursor() as cursor:
            sql = f"select year_id from database.customs_data order by year_id desc limit 1"
            cursor.execute(sql)
            datareader = cursor.fetchall()
            for row in datareader:
                year = row[0]
            connection.close()
            return year
    except Exception as _ex:
        print("Error while working with database: ", _ex)

def checkMonth():
    try:
        connection = psycopg2.connect(
            port=port,
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        with connection.cursor() as cursor:
            sql = f"select month_id from database.customs_data order by month_id desc limit 1"
            cursor.execute(sql)
            datareader = cursor.fetchall()
            for row in datareader:
                year = row[0]
            connection.close()
            return year
    except Exception as _ex:
        print("Error while working with database: ", _ex)
