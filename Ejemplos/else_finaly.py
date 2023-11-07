def anio_bisiesto():
    try:
        anio = int(input('Ingrese el anio: '))
    except:
        print('No se ingreso un dato valido.')
        return None
    else: #SE EJECUTA EL ELSE CUANDO EL SE EJECUTO EL TRY
        print('El dato es valido')
    finally: #Se ejecutal el finally en cualquier caso
        print('Esta linea siempre se ejecuta')

    if anio % 400 == 0 or (anio%4==0 and anio%100 !=0):
        print(f'El anio {anio} es bisiesto')
    else:
        print(f'El anio {anio} NO es bisiesto')

while(True):
    anio_bisiesto() 