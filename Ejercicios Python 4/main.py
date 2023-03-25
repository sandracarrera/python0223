from Ejercicio2 import sorteo
from Ejercicio4 import Registro
from Ejercicio5 import validar
from Ejercicio3 import pokemon

Opciones="""
    1)EJERCICIO 2
    2)EJERCICIO 3
    3)EJERCICIO 4
    4)EJERCICIO 5
    5)Salir 
"""
print(Opciones)
opt = int(input("Que ejercicio quiere:"))

if type(opt) == int:
    if opt==1:
        sorteo.randomnum()
    elif opt==2:
        msg="""
            "Pokemons región Kanto"
            1) Listar pokemons
            2) Buscar pokemon
            3) Salir    
            """
        pokemon()
        pass
    elif opt==3:
        Registro.texto()
    elif opt==4:
        validar()
    elif opt==5:
        print("Ingrese una opcion correcta")
else:
    print("ingrese un valor entero ,valor no permitido")




        
    