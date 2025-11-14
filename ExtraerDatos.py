
import mysql.connector

# Conón con el serv MySQL Server
conex = mysql.connector.connect(
    host='localhost', user='root', passwd='',  db='practica' )

# Consulta SQL que ejecuta, en este caso un select
sqlSelect = """SELECT  *  FROM clientes """
           
# conecta con el servidor MySQL
cursor = conex.cursor()

# El cursor, ejecuta la consulta SQL
cursor.execute(sqlSelect)

# Guarda el resul de la consulta en una variable
resulSQL = cursor.fetchall()

# Cierra el cursor y la conexión con MySQL
cursor.close()
conex.close()

# Muestra el resultado por pantalla
print(resulSQL)
