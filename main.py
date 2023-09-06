from readchar import readkey, key

nombre = input("Ingrese su nombre: ")
bienvenida = print("Bienvenido! "+str(nombre))

while True:
    k = readkey()
    print("*")
    if k == key.UP:
        break