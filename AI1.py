import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2
dado1, dado2 = lanzar_dados()
print(f"Dado 1: {dado1}")
print(f"Dado 2: {dado2}")
print(f"Suma total: {dado1 + dado2}")
