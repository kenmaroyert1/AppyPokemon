¡Buenísimo! 🚀
Ya tienes la **documentación de tu proyecto de bandas**, pero como lo migraste a **Pokémon**, podemos adaptar todo el README para que sea coherente con la nueva API.

Aquí te dejo la versión ajustada a **AppyPokemon**:

---

# AppyPokemon

Ingeniería Web - Trabajo

# CRUD REST API

Este proyecto es una API RESTful desarrollada en Python usando Flask, diseñada para gestionar **Pokémon y sus tipos**.
Los datos se almacenan en memoria (no se utiliza base de datos) y la API permite realizar operaciones CRUD sobre los Pokémon.

## Estructura del Proyecto

* **src/app.py**: Punto de entrada de la aplicación Flask. Define todos los endpoints de la API y almacena los datos en memoria.
* **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.
* **curl_examples.sh**: Ejemplos de comandos `curl` para probar la API.

## Endpoints disponibles

* `GET /pokemons`: Obtiene la lista de todos los Pokémon.
* `GET /pokemons/<id>`: Obtiene la información de un Pokémon por su ID.
* `POST /pokemons`: Crea un nuevo Pokémon. Requiere un JSON con `name` y `types` (lista de tipos).
* `PUT /pokemons/<id>`: Actualiza el nombre o los tipos de un Pokémon existente.
* `DELETE /pokemons/<id>`: Elimina un Pokémon por su ID.

## Ejemplo de uso

* **Obtener todos los Pokémon:**

  ```bash
  curl -i http://localhost:6000/pokemons
  ```

* **Obtener un Pokémon por ID:**

  ```bash
  curl -i http://localhost:6000/pokemons/1
  ```

* **Crear un nuevo Pokémon:**

  ```bash
  curl -i -X POST http://localhost:6000/pokemons \
  	-H "Content-Type: application/json" \
  	-d '{"name": "Bulbasaur", "types": ["Planta", "Veneno"]}'
  ```

* **Actualizar un Pokémon existente:**

  ```bash
  curl -i -X PUT http://localhost:6000/pokemons/2 \
  	-H "Content-Type: application/json" \
  	-d '{"name": "Charizard", "types": ["Fuego", "Volador"]}'
  ```

* **Eliminar un Pokémon:**

  ```bash
  curl -i -X DELETE http://localhost:6000/pokemons/3
  ```

## Requisitos

* Python 3.12+

## Instalación y ejecución

1. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta la aplicación:

   ```bash
   python3 src/app.py
   ```

## Notas

* Los datos se almacenan en memoria, por lo que se perderán al reiniciar la aplicación.
* Los endpoints devuelven respuestas en formato JSON y usan los códigos de error HTTP apropiados.
* Puedes modificar el código para agregar más funcionalidades (por ejemplo: habilidades, evoluciones o regiones).

---

🎮 ¡Atrápalos todos con Flask! ⚡🔥💧🌿

---

¿Quieres que también te prepare el **`curl_examples.sh` completo para Pokémon** con los 10 casos de prueba que hicimos antes?
