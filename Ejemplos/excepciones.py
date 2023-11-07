#Uso SIN try(except)

'''def dividir(a,b):
    if(b==0):
        return None
    return a/b
while True: 
    a= int (input('Ingrese el denominador: '))
    b= int (input('Ingrese el numerador: '))
    print(dividir(a,b))'''

#Uso CON try(except)

def dividir(a,b):
    try:
        return a/b
    except Exception as error:
        print("La operacion no se pudo realizar por: ", error)
    
while True: 
    a= int (input('Ingrese el Numerador: '))
    b= int (input('Ingrese el Denominador: '))
    print(dividir(a,b))
