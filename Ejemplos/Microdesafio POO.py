class Auto:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

auto = Auto("Toyota", "Corolla")

print(f"Marca: {auto.marca}")
print(f"Modelo: {auto.modelo}")