import requests

url='https://pokeapi.co/api/v2/pokedex/2/'

data=requests.get(url).json()
listPokemon=data['pokemon_entries']
#print(type(listPokemon))

#print(listPokemon[0]['pokemon_species'])

# for i,value in enumerate(listPokemon):
#     name=value['pokemon_species']['name']
#     print(i,"=>",name)

## hacer un buscador 
#urlDemo="https://pokeapi.co/api/v2/pokemon/bulbasaur"
url="https://pokeapi.co/api/v2/pokemon/"

msg="""
    "Pokemons región Kanto"
    1) Listar pokemons
    2) Buscar pokemon
    3) Salir    
    """
def pokemon():
     while True:
          print(msg)
          opcion=float(input("Ingrese el numero de operacion a realizar: "))
     
          if opcion ==1:
                    for i,value in enumerate(listPokemon):
                         name=value['pokemon_species']['name']
                         print(i+1,"=>",name)
          
          if opcion ==2:
               num = int(input("Ingrese el numero de pokedex del pokemon: "))
               for i,value in enumerate(listPokemon):
                    name=value['pokemon_species']['name']
                    if num == i+1:
                         print(f"El Pokemon {num} es: ")
                         print(num,"-",name)
               pass
          
          if opcion ==3:
               print("Atrapalos a todos")
               break
          