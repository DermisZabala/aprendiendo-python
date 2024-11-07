import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

# utilizando unique para que el nombre del articulo no se repita
'''miCursor.execute("""
    CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
""")'''

'''productos=[
    ("Pelota", 20, "Juegueteria"),
    ("Pantalon", 15, "Confeccion"),
    ("Destornillador", 25, "Ferreteria"),
    ("Jarron", 45, "Ceramica")
]'''

# cuando el id es incrementable se debe utilizar NULL
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)



# actualizando los datos de los registros
#miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO = 'Pelota'")



# eliminando registro por el ID
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")


"""REALIZANDO ACTUALIZACIONES"""
miCursor.execute("UPDATE PRODUCTOS SET SECCION='Jugueteria' WHERE ID=1")
miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 39 WHERE ID=5")

# ver los registros filtrado con WHERE
miCursor.execute("SELECT * FROM PRODUCTOS")

productos = miCursor.fetchall()

for i in productos:
    print(i)

miConexion.commit()

miConexion.close()