###### EJERCICIO 3
## mayor

primero = int(input("ingrese el primero numero: "))
segundo = int(input("ingrese el segundo numero: "))

def mayor():
    if (primero > segundo):
        print(f"el mayor es:{primero}")
    elif (primero < segundo):
        print(f"el mayor es:{segundo}")
    else:
        print("son iguales")
mayor()
