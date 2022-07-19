class Coche():

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.__largoChasis=250
        self.__numeroRuedas=4
        self.__anchoChasis=20
        self.__enmarcha=False
        self.acelera=False

    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha==True):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo va mal"    
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene ",self.__largoChasis, self.__numeroRuedas, "ruedas. Un anche de ",self.__anchoChasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")  

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"  

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False




miCoche=Coche()    
print(miCoche.arrancar(True))
miCoche.estado()


