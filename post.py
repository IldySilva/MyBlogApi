import psycopg2

hostname = "localhost"
database = "test"
pwd = "root"
port = 5432

conexion = psycopg2.connect(
    host=hostname,
    dbname=database,
    password=pwd,
    port=port,
    user="postgres"

)
cursor = conexion.cursor(

)
cursor.execute("select id from person")
data = cursor.fetchall()
for c in data:
    print(c)
conexion.commit()
conexion.close()
