import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

nombre = input("Ingrese el nombre del jugador: ")
dado1, dado2 = lanzar_dados()

print("Dado 1:", dado1)
print("Dado 2:", dado2)

if dado1 == 1 and dado2 == 1:
    print("Felicitaciones", nombre, "Puedes sacar una ficha")
elif dado1 == 2 and dado2 == 2:
    print("Felicitaciones", nombre, "Puedes sacar una ficha")
elif dado1 == 3 and dado2 == 3:
    print("Felicitaciones", nombre, "Puedes sacar una ficha")
elif dado1 == 4 and dado2 == 4:
    print("Felicitaciones", nombre, "Puedes sacar una ficha")
elif dado1 == 5 and dado2 == 5:
    print("Felicitaciones", nombre, "Puedes sacar una ficha")
elif dado1 == 6 and dado2 == 6:
    print("Felicitaciones", nombre, "Puedes sacar una ficha")
else:
    print("Turno del siguiente jugador")
