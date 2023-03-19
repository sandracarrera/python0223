####### EJERCICIO 2

class producto:

    def __init__(self, product, precio, marca):
        self.product = product
        self.precio = precio
        self.marca = marca
        print('Se ha agregado el producto:', self.product)

    def __str__(self):
        return '{} - {} - {}'.format(self.product, self.marca, self.precio)
        


class catalogo:

    productos_guardados = []

    def __init__(self, productos=[]):
        self.productos_guardados = productos

    def agregar(self, p):  
        self.productos_guardados.append(p)

    def mostrar(self):
        for p in self.productos_guardados:
            print(p) 
    
p = producto("llanta", 175 , "susuki")
c = catalogo([p])  
c.mostrar()

c.agregar(producto("espejos", 80, "lineo"))  # Añadimos otra
c.mostrar()