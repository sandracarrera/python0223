########## EJERCICIO 7

texto = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas Letraset, las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum"


Menu= """
1)Cambiar el texto a MAYUSCULA
2)Saber la longitud del texto
3)buscar cuantas veces sale una palabra
"""
print(Menu)
opcion=int(input("Elija su opcion:"))

if opcion==1:
    print(texto.upper())

elif opcion ==2:
    print(len(texto))

elif opcion == 3:
        palabra = input("que palabra quiere buscar?:")
        print(texto.count(palabra))

else:
    print("adios")




