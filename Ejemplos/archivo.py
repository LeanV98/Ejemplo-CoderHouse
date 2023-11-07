try:
    f= open("archivo.txt","w")
except Exception as err:
    print("El archivo no se pudo abrir", err)

f.write("Primera linea de text\n")
f.write("Segunda linea de textp\n")
f.close()
