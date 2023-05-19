import csv
import os
import psycopg2
from config import host, user, password, db_name, port

import CLASSES.DataLoad

region_id = None
tnved_id = None
unit_id = None
stoim = None
netto = None
kol = None
year_id = None
list_countries_id = None
month_id = None
export = None

tnved_reference = None


def main():
    ReadingData()
    try:
        os.remove('DataContainer/DATTSVT.csv')
        print("Successfully delete temp files")
    except Exception as _ex:
        print("Error while deleting temp files", _ex)

def ReadingData():
    try:
        with open('DataContainer/DATTSVT.csv', newline='', encoding="utf8") as csvfile:
            datareader = csv.reader(csvfile, delimiter='	')
            count = 0
            print("Start working with data")
            for row in datareader:
                if count > 0:
                    TransformationData(row)
                count += 1
            print("Successfully working with csv file. Totally records: ", count)

    except Exception as _ex:
        print("Error while working with csv file: ", _ex)
        exit()


def TransformationData(stringofData):
    try:
        if stringofData[0] == 'ЭК':
            export = True
        else:
            export = False
        month_id = int(stringofData[1].split('/')[0])
        year_id = int(stringofData[1].split('/')[1])
        if stringofData[2] == 'NNN':
            list_countries_id = 'NN'
        else:
            list_countries_id = stringofData[2]
        tnved_id = stringofData[3]
        if stringofData[4] == '':
            unit_id = None
        else:
            try:
                connection = psycopg2.connect(
                    port=port,
                    host=host,
                    user=user,
                    password=password,
                    database=db_name
                )
                with connection.cursor() as cursor:
                    data = (Units(stringofData[4]).lower())
                    sql = f"select id from knowledgebase.units where raw ILIKE '{data}'"
                    cursor.execute(sql)
                    datareader = cursor.fetchall()
                    for row in datareader:
                        unit_id = row[0]
                    connection.close()
            except Exception as _ex:
                print("Error while working with database: ", _ex)
                exit()
        stoim = stringofData[5].replace(',', '.')
        netto = stringofData[6].replace(',', '.')
        kol = stringofData[7].replace(',', '.')

        try:
            connection = psycopg2.connect(
                port=port,
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            with connection.cursor() as cursor:
                if stringofData[8].split('- ')[1] == 'ГОРОД МОСКВА СТОЛИЦА РОССИЙСКОЙ ФЕДЕРАЦИИ ГОРОД ФЕДЕРАЛЬНОГО ЗНАЧЕНИЯ' or stringofData[8].split('- ')[1] == 'ГОРОД САНКТ-ПЕТЕРБУРГ ГОРОД ФЕДЕРАЛЬНОГО ЗНАЧЕНИЯ':
                    data = stringofData[8].split(' ')[3]
                else:
                    if stringofData[8] == '67000 - СЕВАСТОПОЛЬ - ГОРОД ФЕДЕРАЛЬНОГО ЗНАЧЕНИЯ':
                        data = stringofData[8].split(' ')[2]
                    else:
                        data = stringofData[8].split(' - ')[1]
                if data == 'РЕСПУБЛИКА ТАТАРСТАН (ТАТАРСТАН)' or data == 'РЕСПУБЛИКА АДЫГЕЯ (АДЫГЕЯ)' or data == 'ХАНТЫ-МАНСИЙСКИЙ АВТОНОМНЫЙ ОКРУГ (ТЮМЕНСКАЯ ОБЛАСТЬ)' or data == 'ЯМАЛО-НЕНЕЦКИЙ АВТОНОМНЫЙ ОКРУГ (ТЮМЕНСКАЯ ОБЛАСТЬ)' or data == 'НЕНЕЦКИЙ АВТОНОМНЫЙ ОКРУГ (АРХАНГЕЛЬСКАЯ ОБЛАСТЬ)':
                    data = data.split(' (')[0]
                if data == 'ХАНТЫ-МАНСИЙСКИЙ АВТОНОМНЫЙ ОКРУГ':
                    data = data + ' – Югра'
                if data == 'РЕСПУБЛИКА СЕВЕРНАЯ ОСЕТИЯ-АЛАНИЯ':
                    data = 'Республика Северная Осетия – Алания'
                if data == 'МОСКВА' or data == 'САНКТ-ПЕТЕРБУРГ' or data == 'СЕВАСТОПОЛЬ':
                    data = 'г. ' + data
                sql = f"select id from knowledgebase.regions where name ILIKE '{data}'"
                cursor.execute(sql)
                datareader = cursor.fetchall()
                for row in datareader:
                    region_id = row[0]
                connection.close()
        except Exception as _ex:
            print("Error while working with database: ", _ex)
            exit()
    except Exception as _ex:
        print("Error while transforming data: ", _ex)
        exit()

    try:
        CLASSES.DataLoad.insertData(region_id, tnved_id, unit_id, stoim, netto, kol, year_id, list_countries_id, month_id, export)
    except Exception as _ex:
        print(data)
        print("Error while loading data: ", _ex)
        exit()
def Units(edizm):
    try:
        with open('SuppoterFiles/EDIZM.csv', newline='', encoding="utf8") as csvfile:
            datareader = csv.reader(csvfile, delimiter='	')
            count = 0
            for row in datareader:
                if count != 0:
                    if edizm == row[0]:
                        if row[1] == "ШТУКА":
                            return row[1].split('А')[0]
                        else:
                            return row[1]
                count += 1

    except Exception as _ex:
        print("Error while working with EDIZM file:", _ex)
        exit()
