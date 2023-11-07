lista = [1,2,3,4,5]
nombres = ['uno','dos','tres','cuatro','cinco']

dicionario_numeros = dict(zip(nombres,lista))
print (dicionario_numeros)
for numero in dicionario_numeros.values():
    print('Este mensaje es el numero:', numero)
