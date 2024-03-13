from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
#db.resetDatabase()

tipos = ["Grass", "Poison"]
pokemons = db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": True} })
writeAJson(pokemons,"pokemons")

#Pokemons com 2 weaknesses
pokemons = db.collection.find({"weaknesses": {"$size": 2}})
writeAJson(pokemons,"pokemons")

pokemons = db.collection.find({"$or": [{"type":"Fire"},{"weaknesses": "Water"}]})
writeAJson(pokemons,"pokemons")

tipos = ["Fire"]
pokemons = db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": False} })
writeAJson(pokemons,"pokemons")

pokemons = db.collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}})
writeAJson(pokemons,"pokemons")