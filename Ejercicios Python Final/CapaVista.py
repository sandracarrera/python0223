from CapaLogica import *

msg = """
    1)Mostrar provincias según ingresos
    2)Mostrar provincia especifica
    3)Crear db y su tabla 
    4)Mostrar la tabla
    5)Agregar nuevos elementos a la db
    6)Salir
"""

print(msg)
elige = int(input("Ingrese el numero de ejercicio a realizar: "))
general(elige)
