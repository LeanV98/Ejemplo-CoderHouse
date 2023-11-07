#Metodos especiales (Ej: __init__ o __str__)
# __init__ sirve para crear cada una de las instancias de la clase
# __str__ sirve para crear una cadena de texto entendible
# __len__ sirve para devolver el numnero de elementos que tiene el objeto
# __getitem__ sirve para devolver un elemento utilizando corchetes
# __setitem__ sirve para modificar un elemento
# __iter__ sirve para hacer que nuestar clase sea iterable


class Vector:
    def __init__(self, data) -> None:
        self.data=data

    def __str__(self) -> str:
        return (f"El valor de este vector es: {self.data}")
    
    def __len__(self):
        return len(self.data)

    def __getitem__(self, pos):
        return self.data[pos]
    
    def __setitem__(self, pos, num):
        self.data[pos]=num
    
    def __iter__(self):
        for pos in range(0,len(self.data)):
            yield (f"Valor[{pos}]: {self.data[pos]}")
        
        

vector = Vector([1,2,3])

print(vector)
print(f"El largo del vector es: {len(vector)}")
print(vector[0])
vector.__setitem__(0,10)
print(vector)

for i in vector:
    print (i)