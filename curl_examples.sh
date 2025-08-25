# 1. Obtener todos los Pokémon
curl -i http://localhost:6000/pokemons

# 2. Obtener un Pokémon por ID (ejemplo: 1 - Pikachu)
curl -i http://localhost:6000/pokemons/1

# 3. Obtener un Pokémon inexistente (ejemplo: 99)
curl -i http://localhost:6000/pokemons/99

# 4. Crear un nuevo Pokémon
curl -i -X POST http://localhost:6000/pokemons \
  -H "Content-Type: application/json" \
  -d '{"name": "Bulbasaur", "types": ["Planta", "Veneno"]}'

# 5. Crear un Pokémon con datos incompletos
curl -i -X POST http://localhost:6000/pokemons \
  -H "Content-Type: application/json" \
  -d '{"name": "Eevee"}'

# 6. Actualizar un Pokémon existente (ejemplo: 2 - Charmander)
curl -i -X PUT http://localhost:6000/pokemons/2 \
  -H "Content-Type: application/json" \
  -d '{"name": "Charizard", "types": ["Fuego", "Volador"]}'

# 7. Actualizar un Pokémon inexistente (ejemplo: 99)
curl -i -X PUT http://localhost:6000/pokemons/99 \
  -H "Content-Type: application/json" \
  -d '{"name": "MissingNo", "types": ["???"]}'

# 8. Eliminar un Pokémon existente (ejemplo: 3 - Squirtle)
curl -i -X DELETE http://localhost:6000/pokemons/3

# 9. Eliminar un Pokémon inexistente (ejemplo: 99)
curl -i -X DELETE http://localhost:6000/pokemons/99

# 10. Crear un Pokémon con un arreglo vacío de tipos
curl -i -X POST http://localhost:6000/pokemons \
  -H "Content-Type: application/json" \
  -d '{"name": "Magikarp", "types": []}'
