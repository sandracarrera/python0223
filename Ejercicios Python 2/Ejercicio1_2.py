#######EJERCICIO 1

Menu= """
1)Hacer un cuadrado
2)Saber los Multiplos
3)Identificar los Mayores de edad
"""
print(Menu)
opcion=int(input("Elija su opcion:"))

#1.1 un cuadrado
if opcion==1:
    cuadrado = int(input('Ingrese la medida del lado del cuadrado: '))
    for f in range(0, cuadrado):
        for c in range(0, cuadrado):
            print('*', end='')
        print()
        pass

#1.2 multiplo de 2
elif opcion ==2:
    lista=[1,2,35,28,97]
    for numero in lista:
        if (numero % 2 == 0):
            print(f"es multiplo: {numero}")


#1.3 mayores de edad
elif opcion == 3:
    personas = [('Luis','24'),('Miguel','26'),('Kiara','11')]
    for edad in personas:
        if int(edad[1])>=18:
            print(f"Mayores de edad:{edad}")

   

        

