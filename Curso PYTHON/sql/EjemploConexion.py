import sqlite3

# creando la base de datos y abrir la conexion

miConexion = sqlite3.connect("PrimeraBasedeDatos")

# creando tabla
miCursor = miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (nombre_articulo VARCHAR(50), precio INTEGER, seccion VARCHAR(20))")

# insertando datos en la tabla productos
miCursor.execute("INSERT INTO PRODUCTOS VALUES('Balon', 15, 'Deportes')")

# confirmar los cambios que se realizaron en la base de datos
miConexion.commit()

miConexion.close() #cerrando la conexion