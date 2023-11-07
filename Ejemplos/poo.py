class Perro:

    especie = "Mamifero"

    def __init__(self,nombre, raza): #Constructor
        #Atributos de instancia
        self.nombre = nombre
        self.raza = raza
    
    def ladrar(self): #Definicion de metodo
        return ("Este perro acaba de ladrar")
       

    def caminar(self, pasos): #Definicion de metodo con varaible
        return (f"Este peroacaba de caminar {pasos} pasos")


perro1 = Perro("Sam","Caniche")


print(f"Su nombre es: {perro1.nombre}")
print(f"Su raza es: {perro1.raza}")
print(f"Su especie es: {perro1.especie}")
print(perro1.ladrar()) #Se imprime como si fuera una funcion
print(perro1.caminar("23")) #Se imprime como si fuera una funcion
