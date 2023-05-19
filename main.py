import CLASSES.DataTransform
import CLASSES.DataExtract

"""import psycopg2
from config import host, user, password, db_name, port

print(host, user, password, db_name, port)

try:
    print(host, user, password, db_name, port)
    connection = psycopg2.connect(
        port=port,
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")
    connection.close()
except Exception as _ex:
    print("[Info] Error while working with PostgreSQL", _ex)"""

while (CLASSES.DataExtract.main() > 1):
    CLASSES.DataTransform.main()