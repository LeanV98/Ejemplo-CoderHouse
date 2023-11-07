cantidad = int(input('Ingrese cantidad de numeros a ingresar: '))
lista = []

for i in range(cantidad): 
    numero=int(input('Ingrese un numero: '))
    lista.append(numero)

print("El promedio es: ",(sum(lista)/cantidad))
