#Tarea pokemones - Flavia Aray

#Se pregunta el sexo y se saluda de acuerdo a la respuesta
sexo = input("¿Cuál es tu sexo? (M o F) ")

if sexo == "M":
    print("Hola, entrenador!")
else:
    print("Hola, entrenadora!")

#Se pregunta la región y se respnde con un mensaje
region = input("¿De qué región eres? ")
print("¡ Me encanta", region, "!")

#Se pregunta el Pokémon preferido y se responde refiriendose a su tipo
pokemon = input("¿Cuál es tu Pokémon preferido? (Charmander, Bulbasaur o Squirtle) ")
if pokemon == "Charmander":
    print("¡De fuego es genial!")
elif pokemon == "Bulbasaur":
    print("¡De planta es genial!")
else:
    print("¡De agua es genial!")
    
