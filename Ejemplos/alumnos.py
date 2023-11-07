class Alumno:

    def __init__(self,dni,nombre, apellido,edad): #Constructor
        #Atributos de instancia
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self) -> str:
        return self.nombre + " " + self.apellido
    
    def estudiando(self):
        print("El alumno", self.nombre, "esta estudiando")

    def crecer(self):
        self.edad+=1
        
        print("El alumno", self.nombre, "ahora tiene", self.edad, "anios")