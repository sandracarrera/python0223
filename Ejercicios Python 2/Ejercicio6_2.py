######### EJERCICIO 6
#EVENTO
concierto={
    'artista':"harry style",
    'precio':700,
    'aforo':1000,
    'lugar':"Parque de la Exposicion"
}

def buscarEvento(artista):
    if concierto['artista'] == artista:
        return concierto
    else:
        return False

def verificarAforo(conciert:dict)->int:
    if conciert['aforo']:
        return conciert['aforo']
    
def verificarLugar(lug:dict):
    if lug['lugar'] :
        return lug['lugar']
    else:
        return False
    

def main():
    nameConcierto=input('Nombre del concierto que desea:')
    myConcert=dict()
    if buscarEvento(nameConcierto):
        myConcert=buscarEvento(nameConcierto)
    else:
        print("No existe el concierto :C")

    #verificar aforo
    if verificarAforo(myConcert):
        print(f"El aforo para el concierto es {verificarAforo(myConcert)}")
    else:
        print("No hay aforo disponible")
    
    #verificar Lugar
    if verificarLugar(myConcert):
        print(f"El concierto se llevara acabo en {verificarLugar(myConcert)}")
    else:
        print("Concierto Cancelado")

main()