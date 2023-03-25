from datetime import datetime

class Registro:

    def texto():
        nom = input("nombre del archivo:")
        arch = open(nom,'w')
        arch.write('')
        print("archivo creado")

        mensaje = input("introdusca su mensaje:")
        fecha = datetime.now()
        hoy = fecha.strftime("%d/%m/%Y %H:%M:%S")
        men=arch.write(f"{hoy} - Archivo: {nom} - Mensaje: {mensaje}")

        arch = open(nom,'r')
        valor= arch.read(men)
        print(valor)
        arch.close()
    """ texto() """
    

    


    


    




  