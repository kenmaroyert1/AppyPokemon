from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos simulados: Pokémon y sus tipos
pokemons = [
    {
        "id": 1,
        "name": "Pikachu",
        "types": ["Eléctrico"]
    },
    {
        "id": 2,
        "name": "Charmander",
        "types": ["Fuego"]
    },
    {
        "id": 3,
        "name": "Squirtle",
        "types": ["Agua"]
    }
]

# Obtener todos los Pokémon
@app.route('/pokemons', methods=['GET'])
def get_pokemons():
    return jsonify(pokemons), 200

# Obtener un Pokémon por ID
@app.route('/pokemons/<int:pokemon_id>', methods=['GET'])
def get_pokemon(pokemon_id):
    pokemon = next((p for p in pokemons if p['id'] == pokemon_id), None)
    if pokemon is None:
        return jsonify({'error': 'Pokémon not found'}), 404
    return jsonify(pokemon), 200

# Crear un nuevo Pokémon
@app.route('/pokemons', methods=['POST'])
def create_pokemon():
    if not request.json or 'name' not in request.json or 'types' not in request.json:
        return jsonify({'error': 'Bad request'}), 400
    new_id = max(p['id'] for p in pokemons) + 1 if pokemons else 1
    pokemon = {
        'id': new_id,
        'name': request.json['name'],
        'types': request.json['types']
    }
    pokemons.append(pokemon)
    return jsonify(pokemon), 201

# Actualizar un Pokémon existente
@app.route('/pokemons/<int:pokemon_id>', methods=['PUT'])
def update_pokemon(pokemon_id):
    pokemon = next((p for p in pokemons if p['id'] == pokemon_id), None)
    if pokemon is None:
        return jsonify({'error': 'Pokémon not found'}), 404
    if not request.json:
        return jsonify({'error': 'Bad request'}), 400
    pokemon['name'] = request.json.get('name', pokemon['name'])
    pokemon['types'] = request.json.get('types', pokemon['types'])
    return jsonify(pokemon), 200

# Eliminar un Pokémon
@app.route('/pokemons/<int:pokemon_id>', methods=['DELETE'])
def delete_pokemon(pokemon_id):
    pokemon = next((p for p in pokemons if p['id'] == pokemon_id), None)
    if pokemon is None:
        return jsonify({'error': 'Pokémon not found'}), 404
    pokemons.remove(pokemon)
    return jsonify({'result': 'Pokémon deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)
