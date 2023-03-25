import os 

class Product:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        print('Se agrego el producto: ',self.nombre)

    def __str__(self):
        return 'El producto {} del pais {} tiene el codigo {} '.format(self.nombre, self.codigo.split("-")[0],self.codigo.split("-")[1])

class Show:
    mostrar = []

    def __init__(self, mostrar =[]):
        self.mostrar = mostrar

    def agregar(self, a):
        self.mostrar.append(a)

    def mostrar_all(self):
        for a in self.mostrar:
            print(a)
            
a = Product("Alfajores","Argentina-0010-2023")
b = Show([a])
b.mostrar_all()






        


    



    