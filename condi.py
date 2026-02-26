import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

nombre = input("Ingrese el nombre del jugador: ")

dado1, dado2 = lanzar_dados()

print(f"{nombre} lanzó los dados: {dado1} y {dado2}")

if dado1 == dado2:
    print(f"Felicitaciones {nombre} Puedes sacar una ficha")
else:
    print("Turno del siguiente jugador")
