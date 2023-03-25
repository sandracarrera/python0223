import re

def validar():
    try:
        numero = int(input("Ingrese el numero de celular a validar: "))
    
        if len(str(numero)) == 9:
        
            celular= re.compile(r'\b9[0-9]*\d')
            condicion = celular.match(str(numero))
            if int(bool(condicion)):
                    print(f"El numero {numero} es valido")
            else:
                    print(f"El numero {numero} es invalido")
        else:
            print("El numero es corto")
    except:
             print("Ingrese valores admitidos")

""" validar() """
