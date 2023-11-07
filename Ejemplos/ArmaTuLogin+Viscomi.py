usuarios={}

def registro_usuario():
    nombre = input('Ingrese el nombre de usuario: ')
    contraseña = input('Ingrese la contraseña: ')

    usuarios[nombre]=contraseña

def mostrar_usuario():
    for usuario, contraseña in usuarios.items():
        print(f"Usuario: {usuario}, Contraseña: {contraseña}")

def iniciar_sesion():

    nombre = input('Ingrese el nombre de usuario: ')
    contraseña = input("Ingrese su contraseña: ")
    if nombre in usuarios and contraseña == usuarios[nombre]:
        print("Inicio de sesión exitoso")
    else:
        print("El nombre de usuario o la contraseña son incorrectos")

while True:
    
    try:
        opcion = int (input("¿Qué desea hacer? (1) Registrar usuario, (2) Mostrar usuarios, (3) Iniciar sesión, (4) Salir: "))
    except Exception as error:
        print("La operacion no se pudo realizar por: ", error)
        break
    
    if opcion == 1:
        registro_usuario()
    elif opcion == 2:
        mostrar_usuario()
    elif opcion == 3:
        iniciar_sesion()
    elif opcion == 4:
        break