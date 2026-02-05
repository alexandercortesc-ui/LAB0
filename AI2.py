import random

nombre = input("Ingrese el nombre del jugador: ")

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print(f"{nombre} lanzó los dados: {dado1} y {dado2}")

if dado1 == dado2:
    print(f"Felicitaciones {nombre} Puedes sacar una ficha")
else:
    print("Turno del siguiente jugador")