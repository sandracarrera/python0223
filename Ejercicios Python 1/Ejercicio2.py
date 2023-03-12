## EJERCICIO 2 --- AREA CIRCULO, CUADRADO Y TRIANGULO

Opciones="""
    1)AREA DEL CIRCULO
    2)AREA DEL CUADRADO
    3)AREA DEL TRIANGULO    
"""
print(Opciones)
opt=int(input("Ingrese una opcion que deseas desarrollar:"))

if type(opt) == int:
    if opt==1:
        radio=int(input("Ingresa el radio:"))
        print(f"El area del Circulo es: {radio*radio*3.14}")
    elif opt==2:
        lado=int(input("Ingresa el lado: "))
        print(f"El area del Cuadrado es: {lado*lado}")
    elif opt==3:
        base=int(input("Ingresa la base: "))
        altura=int(input("Ingresa la altura:"))
        print(f"El area del Triangulo es: {(base*altura)/2}")  
    else:
        print("Ingrese una opcion correcta")
else:
    print("ingrese un valor entero ,valor no permitido")