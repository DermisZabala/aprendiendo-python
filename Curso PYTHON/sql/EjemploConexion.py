import sqlite3

# creando la base de datos y abrir la conexion

miConexion = sqlite3.connect("PrimeraBasedeDatos")

# creando tabla
miCursor = miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (nombre_articulo VARCHAR(50), precio INTEGER, seccion VARCHAR(20))")

# insertando datos en la tabla productos
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('Balon', 15, 'Deportes')")

# 3 tuplas dentro de una lista para insertarla en la base de datos
variosProductos=[
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria")
]

# insertando la lista dentro de la base de datos
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS")

# confirmar los cambios que se realizaron en la base de datos
miConexion.commit()

miConexion.close() #cerrando la conexion