class Persona():
    def __init__(self, name, age, hight, city):
        self.__name=name
        self.__age=age
        self.__hight=hight
        self.__city=city
        self.masc=True
    
    def cambioSexo(self, fem):
        self.masc=fem
        if(self.masc):
            return "Es hombre"
        else: 
            return "Es mujer"

    def definicion(self):
        print("Nombre: ", self.__name, "\nEdad: ", self.__age,"\nAltura: ", self.__hight, "\nCiudad: ", self.__city,)

    def hacerseMayor(self):
        print("La edad de antes era: ", self.__age)
        self.__age=self.__age+1
        print("La edad de ahora es: ", self.__age)

class Niño(Persona):
    def __init__(self, name, age, hight, city, clase, numeroClase):
        super().__init__(name, age, hight, city)
        self.__clase=clase
        self.__numeroClase=numeroClase
    
    def definicion(self):
        super().definicion()
        print("Va a la clase: ", self.__clase, "Numero: ",self.__numeroClase)

persona=Persona("Antonio", 34, 1.50, "Alicante")
print(persona.cambioSexo(False))
persona.hacerseMayor()
persona.definicion()
print("Cambiamos a clase niño---------")
niño=Niño("Pablo", 2, 1.1, "Alicante", "1C", 25)
niño.definicion()


