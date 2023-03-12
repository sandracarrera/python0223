#EJERCICIO 8 -- CONTRASEÑA

contra = "contraseña"
password = input("Introduzca la contraseña: ")
if contra == password.lower():
    print("Contaseña Correcta")
    print("Usuario Detectado")
    print("Bienvenido")
else:
    print("Contraseña Incoincide")
    print("Alerta De Intruso")