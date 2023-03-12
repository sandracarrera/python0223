########## EJERCICIO 9

### Minisistema
roles=['admin','vendedor','inventario']

sistema={
    "nombre":"tienda",
    "usuarios":[
        {
            'name':"",
            'password':"",
            'rol':"" ##vendedor ,administrador ,inventario
        }
    ],
    "sedes":[{
        "nombreSede":"",
        "ubicacion":""
    }],
    "productos":[
    {
        "nombre":"",
        "precio":"",
        "stock":""
    }]
}
##### funciones
## karen vera
def agregarUsuario():
    nameUsuario=input("ingrese el nombre de usuario")
    password=input("ingrese su password")
    while True:
        rol=input("ingrese su rol")
        if rol in roles:
            break
        else:
            print("ingrese un rol correcto",roles)
    
    dictUser={
        'name':nameUsuario,
        'password':password,
        'rol':rol
    }
    sistema['usuarios'].append(dictUser)
###
def eliminarUsuario():
    usuarioPorEliminar=input("ingrese usuario por eliminar")
    for i,valor in enumerate(sistema['usuarios']):
        if valor['name']==usuarioPorEliminar:
                ## ingresar password para verificar que es correcto
                sistema['usuarios'].remove(i)
    ## remove
    pass
###
def obtenerRol(usuario):
    rol=""
    for i,valor in enumerate(sistema["usuarios"]):
        if valor['name']==usuario:
            rol=valor['rol']
    return rol
####
def agregarSedes():
    usuario=input("ingresa usuario")
    rol=obtenerRol(usuario)
    if rol=='admin':
        sede=input("ingrese sede")
        ubicacion=input("ingrese ubicacion")
        dictSede={
            'sede':sede,
            'ubicacion':ubicacion
        }
        sistema["sedes"].append(dictSede)
    else:
        print("no es un rol permitido")

#####
########### SANDRA CARRERA ABILA
def agregarProductos():
    usuario=input("ingresa usuario")
    rol=obtenerRol(usuario)
    if rol=='admin':
        nombre=input("ingrese nombre del producto:")
        precio=int(input("ingrese precio del producto:"))
        stock=int(input("ingrese stock del producto:"))
        dictProducto={
            'nombre':nombre,
            'precio':precio,
            'stock':stock
        }
        sistema["productos"].append(dictProducto)
    else:
        print("no es un rol permitido")

#####
def cambiarStock():
    usuario=input("ingresa usuario")
    rol=obtenerRol(usuario)
    if rol=='admin':
        print(sistema["productos"])
        valores = input("cambiar el stock:")
        for valor in sistema["productos"]:
            valor['stock'] = valores
            print(sistema["productos"])

pass


agregarUsuario()
print(sistema)


agregarProductos()
print(sistema)

cambiarStock()
print(sistema)

