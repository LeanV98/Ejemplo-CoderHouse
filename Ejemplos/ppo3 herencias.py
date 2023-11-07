class Animal:
    def __init__(self,especie,edad) -> None: #Atributos de la clase padre
        self.especie=especie
        self.edad= edad
    def hablar(self): #Defino metodos
        pass
    def caminar(self):
        pass
    def describeme(self):
        print("Soy un animal del tipo:",type(self).__name__)


class Perro(Animal):
    def __init__(self, especie, edad,dueño) -> None:
        super().__init__(especie, edad)
        self.dueño=dueño

    def hablar(self):
        print("guau guau")

    def caminar(self):
        print("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("muuu")

    def caminar(self):
        print("Caminando con 4 patas")


class Abeja(Animal):
    def hablar(self):
        print("Bzzzz")

    def caminar(self):
        print("Volando")

    def picar(self):
        print("picando")



perro1=Perro("Mamifero",2,"")

mi_vaca=Vaca("Mamifero",10)

mi_abeja=Abeja("Insecto",1)

perro1.describeme()
perro1.hablar()
mi_vaca.hablar()
mi_abeja.hablar()   

mi_perro=Perro("Mamifero",3,"Carlos")
print(mi_perro.dueño)