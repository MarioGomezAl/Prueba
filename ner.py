import pickle

class Persona():

    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una nueva persona: ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas():

    personas=[]

    def __init__(self):
        listaDePersonas=open("ficheroExterno","ab+")
        listaDePersonas.seek(0)

        try:
            self.personas=pickle.load(listaDePersonas)
            print("{} personas".format(len(self.personas)))
        
        except:
            print("fichero vacio")
        
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonas()
    
    def mostrarPersonas(self):
        for c in self.personas:
            print(c)
    
    def guardarPersonas(self):
        listaDePersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
    def mostrarInfo(self):
        print("Info: ")
        for p in self.personas:
            print(p)

miLista=ListaPersonas()
p=Persona("Sandra", "Fem", 29)
miLista.agregarPersonas(p)
miLista.mostrarInfo()
miLista.mostrarPersonas()
