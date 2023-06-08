import psycopg2

connection = psycopg2.connect(
    user='postgres',
    password='postgres',
    host='127.0.0.1',
    port='5432',
    database='teachers_subjects'
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM teachers;")

result = cursor.fetchall()
print(result)

cursor.close()
connection.close()