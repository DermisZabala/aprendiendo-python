import pickle

class Personas:
    def __init__(self, nombre, sexo, edad):
        self.nombre = nombre
        self.sexo = sexo
        self.edad = edad

        print("Se creo una persona llamada {}".format(self.nombre))

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.sexo, self.edad)

class ListaPersona:
    miListaPersonas = []

    def __init__(self):
        archivo = open("GuardadoPermanente", "ab+")
        try:
            archivo.seek(0)
            self.miListaPersonas = pickle.load(archivo)
            print("Se al cargado correctamente los datos {} veces".format(len(self.miListaPersonas)))
        except:
            print("El archivo esta vacio")
        finally:
            archivo.close

    def AgregarPersona(self, p):
        self.miListaPersonas.append(p)
        self.cargando_los_datos_del_archivo()

    def RecorrerListaPersona(self):
        for p in self.miListaPersonas:
            print(p)

    def agregando_al_archivo(self):
        archivo = open("GuardadoPermanente", "wb")
        pickle.dump(self.miListaPersonas, archivo)

    def cargando_los_datos_del_archivo(self):
        print("La informacion del fichero externo es la siguiente:")
        for p in self.miListaPersonas:
            print(p)


miLista = ListaPersona()
personas = Personas("Juan", "M", 34)
miLista.AgregarPersona(personas)

miLista.agregando_al_archivo()

