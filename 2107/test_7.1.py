
#https://pokeapi.co/api/v2/pokemon/charizard
import requests

#200: Ok
#404: de permisos
#500: Error con el servidor

res = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")

print(res.status_code)
print(res.headers)
json = res.json()

print(json)