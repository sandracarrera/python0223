## EJERCICIO 3 - SUMA, RESTA, MULTIPLICACION, DIVISION Y DIVISION ENTERA

numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero:"))
numero3=int(input("Ingrese el tercer numero:"))

if (numero2==0):
    print("No puede ser cero")
elif(numero3==0):
    print("No puede ser cero")
else:
    print(f"La suma de los tres numeros es: {numero1+numero2+numero3}")
    print(f"La resta de los tres numeros es: {numero1-numero2-numero3}")
    print(f"La multiplicacion de los tres numeros es: {numero1*numero2*numero3}")
    print(f"La division de los tres numeros es: {numero1/numero2/numero3}")
    print(f"La division de los tres numeros es: {numero1//numero2//numero3}")
    