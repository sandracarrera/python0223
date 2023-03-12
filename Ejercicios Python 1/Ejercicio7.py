##EJERCICIO 7 -- COMPARACION DE NUMEROS

numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))

if (numero1 == numero2):
    print("Los numeros son iguales")
elif (numero1 != numero2):
    print("los numeros son diferentes")
    if(numero1 > numero2):
        print("El primer numero es mayor que el segundo")
    else:
        print("El primer numero es menor que el segundo")
else:
    print("Vuelva a intentarlo")
    
