######### EjercicioS Finales 1,2,3 SANDRA CARRERA ABILA
from CapaModelo import *

def general(opcion:int):
    match opcion:
        case 1:
            mostrar_provincia()
            print("se ejecuto caso 1")
        
        case 2:
            provincia_especifica()
            print("se ejecuto caso 2")

        case 3:
            db_tabla()
            print("se ejecuto caso 3")
            
        case 4:
            mostrar_tabla()
            print("se ejecuto caso 4")
            
        case 5:
            agregar_nuevo()
            print("se ejecuto caso 5")

        case 6:
            salida()
            print("bye bye")
    