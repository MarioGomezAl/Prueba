class Persona():

    def __init__(self, nombre, edad, lugarResidencia):
        self.nombre=nombre
        self.edad=edad
        self.lugarResidencia=lugarResidencia

    def descripcion(self):

        print("Nombre: ", self.nombre, " Edad: ",
        self.edad, " Residencia" ,self.lugarResidencia)

class Empleado(Persona):

    def __init__(self, salario, antigüedad, nombreEmpleado, edadEmpleado, residenciaEmpleado):

        super().__init__(nombreEmpleado, edadEmpleado, residenciaEmpleado)
        self.salario=salario
        self.antigüedad=antigüedad
    
    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, "AntigÜedad. ", self.antigüedad)

persona=Empleado(1500,10, "Manuel", 35, "Albacete")
persona.descripcion()

