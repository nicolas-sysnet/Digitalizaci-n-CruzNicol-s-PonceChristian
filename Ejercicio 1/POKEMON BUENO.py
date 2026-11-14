
pokedex = []

respuesta = input("¿Quieres introducir un pokémon? (Sí (s), No (n)): ").lower()

while respuesta != "s" and respuesta != "n":
    print("Introduce un carácter válido")
    respuesta = input("¿Quieres introducir un pokémon? (Sí (s), No (n)): ").lower()

while respuesta == "s":

    nombrepokemon = input("Introduce el nombre del Pokémon: ")
    tipopokemon = input("Introduce el tipo del Pokémon: ")

    pokemon = {
        "nombre": nombrepokemon,
        "tipo": tipopokemon
    }

    pokedex.append(pokemon)

    respuesta = input("¿Quieres introducir otro pokémon? (Sí (s), No (n)): ").lower()

    while respuesta != "s" and respuesta != "n":
        print("Introduce un carácter válido")
        respuesta = input("¿Quieres introducir otro pokémon? (Sí (s), No (n)): ").lower()

if respuesta == "n":
    print("Muchas gracias por jugar")

print("\n--- POKÉDEX ---")

for pokemon in pokedex:
    print(f"Nombre: {pokemon['nombre']} | Tipo: {pokemon['tipo']}")
