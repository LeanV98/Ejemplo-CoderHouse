class Persona():
    def __init__(self) -> None:
        self.cedula = 12345678
    def mensaje(self):
        print("Mensaj desde la clase Persona")

class Obrero():
    def __init__(self):
        self.__especialista = 1 
    def mensaje(self): #Aqui tenemos el metodo plimorfico 
        print("Mensaje desde la clase Obrero")

persona1 = Persona()
persona1.mensaje()
#mensaje desde la clase Persona

obrero1 = Obrero()
obrero1.mensaje()
#mensajde desde la clase Obrero

class Pato():
    def hablar(self ):
        print("Cuack Cuack")
class Vaca():
    def hablar(self ):
        print("Muu Muu")
class Gato():
    def hablar(self ):
        print("Miau Miau")

pato = Pato()
pato.hablar()

def llama_hablar(x):
    x.hablar()

lista = [Pato(), Gato(), Vaca()]
#for animal in lista:
 #   animal.hablar()    


class Animal:
    def hablar(self):
        ...

for animal in Pato(), Gato():
    animal.hablar()