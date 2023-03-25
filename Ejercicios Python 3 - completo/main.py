import os
from Ejercicio2 import producto,catalogo
from Ejercicio3 import divisiones
from Ejercicio4 import Product,Show

Opciones="""
    1)EJERCICIO 2
    2)EJERCICIO 3
    3)EJERCICIO 4
    4)EJERCICIO 5
    5)Salir 
"""
print(Opciones)
opt=int(input("Que ejercicio quiere:"))

if type(opt) == int:
    if opt==1:
        p = producto("llanta", 175 , "susuki")
        c = catalogo([p])  
        c.mostrar()
        
        c.agregar(producto("espejos", 80, "lineo"))  # Añadimos otra
        c.mostrar()
    
    elif opt==2:
        divisiones()
    
    elif opt==3:
        a = Product("Alfajores","Argentina-0010-2023")
        b = Show([a])
        b.mostrar_all()

    elif opt==4:
        try:
            a = Product("Leche","Peru-0001-2023")
            b = Show([a])
            b.mostrar_all()
        except:
            print("No hay productos")

        else:
            ruta = os.getcwd()
            print(f"La ruta es:{ruta}")
        finally:
            print("Proceso Terminado")
    
    elif opt==5:
        print("Ingrese una opcion correcta, la 6 esta hecha y la 7 no me sale")
else:
    print("ingrese un valor entero ,valor no permitido")


