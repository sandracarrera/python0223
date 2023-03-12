#EJERCICIO 9 -- CADENAS Y TUPLAS

lista = [('Luis','24','12345678'),('Sandra','10','12309845'),('Miguel','26','23456789'),('Liz','58','2356789')]
lista_dni = ['12345678','12309845','23456789','98765432']
 
for valor in lista :
    if int(valor[1]) >= 18 :
        if valor[2] in lista_dni :
            print(valor[0])
            



     



