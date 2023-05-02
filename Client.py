import requests 

url = "https://restexercise1api.azurewebsites.net/api/pokemons"

    #GetALl - henter alle Pokemons Fra REST API
#response = requests.get(url)
#print(response.json())

    #GetById - Henter bestemt pokemon ud fra Id
#response = requests.get(url + "/6")
#print(response.json())

    #Create new Pokemon - laver et ny pokemon objekt
#newPokemon = {'''id":1,'''"pokeDex":15,"pokeName":"Beedrill","level":26,"type":"Bug, Poison"}
#response = requests.post(url, json=newPokemon)
#print(response.json())

    #Updata a Pokemon
#updatePokemon = {"pokeDex":15,"pokeName":"Beedrill","level":26,"type":"Bug, Poison"}
#response = requests.put(url + "/10", json=updatePokemon)
#print(response.json())

    #Delete a Pokemon
#response = requests.delete(url + "/10")
#print(response.json())

