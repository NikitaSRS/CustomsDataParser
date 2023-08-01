import psycopg2
from config import host, user, password, db_name, port
def checkUnique(newLine, month_id, year_id):
    try:
        connection = psycopg2.connect(
            port=port,
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        with connection.cursor() as cursor:
            sql = f"select * from database.customs_data where year_id = {year_id} and month_id = {month_id}"
            cursor.execute(sql)
            datareader = cursor.fetchall()
            count = 0
            for row in datareader:
                if comparisonOfData(newLine, row):
                    count += 1
                    break
            if count == 0:
                connection.close()
                return True
            else:
                connection.close()
                return False
    except Exception as _ex:
        print("Error while working with database: ", _ex)
        exit()
def comparisonOfData(newLine, oldData):
    count = 0
    if newLine[0] == oldData[1]:
        count+=1
    else:
        return False
    if newLine[1] == oldData[2]:
        count += 1
    else:
        return False
    if newLine[2] == oldData[3]:
        count += 1
    else:
        return False
    if newLine[3] == float(oldData[4]):
        count += 1
    else:
        return False
    if newLine[4] == float(oldData[5]):
        count += 1
    else:
        return False
    if newLine[5] == float(oldData[6]):
        count += 1
    else:
        return False
    if newLine[6] == oldData[7]:
        count += 1
    else:
        return False
    if newLine[7] == oldData[8]:
        count += 1
    else:
        return False
    if newLine[8] == oldData[9]:
        count += 1
    else:
        return False
    if newLine[9] == oldData[10]:
        count += 1
    else:
        return False
    return True if count == 10 else False