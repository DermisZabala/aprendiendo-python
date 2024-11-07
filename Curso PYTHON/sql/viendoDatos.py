import sqlite3

miConexion = sqlite3.connect("PrimeraBasedeDatos")

miCursor = miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos = miCursor.fetchall()


for i in variosProductos:
    print("Nombre articulo: {}   \tPrecio: {} \tSeccion: {} " .format(i[0], i[1], i[2]))

miConexion.commit()

miConexion.close()