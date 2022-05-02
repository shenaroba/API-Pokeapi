import requests
import json

def pokeapiv1(url='"http://pokeapi.co/api/v2/pokemon-form/',offset=0):
    url="http://pokeapi.co/api/v2/pokemon-form/"

    args = {'offse' : offset} if offset else{}

    response=requests.get(url, params=args)
    sc=response.status_code
    if sc == 200:
        payload= response.json()
        results = payload.get ('results', [])
        if results:
            for pokemon in results:
                name= pokemon['name']
                print(name)
        
        next=input("continuar con el listado [Y/N]").lower()
        if next== "y":
            pokeapiv1(offset=offset+20)
    else:
        print("No se conecto a la API")
    

amadeo=pokeapiv1()