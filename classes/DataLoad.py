import psycopg2

from config import host, user, password, db_name, port

def insertData(region_id, tnved_id, unit_id, stoim, netto, kol, year_id, list_countries_id, month_id, export):
    try:
        connection = psycopg2.connect(
            port=port,
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as cursor:
            sql = "INSERT INTO database.customs_data (region_id, tnved_id, unit_id, stoim, netto, kol, year_id, list_countries_id, month_id, export) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            data = (region_id, tnved_id, unit_id, float(stoim), float(netto), float(kol), int(year_id), list_countries_id, int(month_id), export)
            cursor.execute(sql, data)
            connection.commit()
            connection.close()

    except Exception as _ex:
        print("Error while working with PostgreSQL", _ex)
        exit()