####### EJERCICIO 2

Biblioteca = {
    "Categoria":["Literatura","Historia","Filosofia","Religion"],
    "Libros":[
        
            ### Titulo, Autor, Disponibilidad 
            ["Cien años de Soledad","Gabriel garcia Marquez", "disponible"],
            ["historia del Peru","Inca Garcilazo de la Vega", "disponible"],
            ["El discurso del metodo", "Rene Descartes", "prestado"],
            ["Cuenta con Jesus","Alicia PAz", "disponible"],
    ],
    "Usuarios":[]
}

def mostrar_categoria():
    print(Biblioteca["Categoria"])

def mostrar_libros ():
    print(Biblioteca["Libros"])

def agregar_usuario():
    print("Escriba salir para dejar de colocar usuarios")
    nom_usuario = input("Agregue el nombre del usuario: ")
    while nom_usuario != "salir":
        Biblioteca["Usuarios"].append(nom_usuario)
        nom_usuario = input("Agregue el nombre del usuario: ")
    print("Estos son los usuarios agregados", '\n',Biblioteca['Usuarios']) 

def cambiar_estado_libro():
    print(Biblioteca["Libros"])
    cambio = input("Ingresar el nombre del libro a cambiar ")
    print("Estados: disponible o prestado")
    estado = input("Ingresar el nuevo estado: ")
    for i in range(0,3):
        if Biblioteca["Libros"][i][0] == cambio:
            Biblioteca["Libros"][i][2] = estado
            print(Biblioteca["Libros"])
        else:
            print("No se encontro el libro")


##mostrar_categoria()
##mostrar_libros()
#agregar_usuario()
cambiar_estado_libro()


