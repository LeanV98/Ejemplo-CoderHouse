divisas = {'Dolar':'$','Euro':'€', 'Libra':'£'}


while(True):
    valor=input('Que divisa quiere ver?: ')
    resultado = divisas.get(valor, 'La moneda no existe')
    print(resultado)
