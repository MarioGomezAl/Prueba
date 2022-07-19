class Vehiculo():

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, ", Modelo: ", self.modelo,"\nEn Marcha: ",
        self.enmarcha)

class Furgoneta(Vehiculo):
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgo esta cargada"
        else:
            return "La furgo no esta cargada"

class Moto(Vehiculo):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Hace el caballito"
    
    def estado(self):
        print("Marca: ", self.marca, ", Modelo: ", self.modelo,"\nEn Marcha: ",
        self.enmarcha,"\n",self.hcaballito)

class VEelectrico():
    def __init__(self):
        self.autonomia=100
    def cargarEnergia(self):
        self.cargando=True

class BiciE(Vehiculo, VEelectrico):
    pass

bii=BiciE("Yamaha","MT")
bii.estado()
miMoto=Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault","Champi")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
