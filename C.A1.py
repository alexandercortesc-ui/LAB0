import random

nombre = input("Ingrese el nombre del jugador: ")
lanzamientos = int(input("Seleccione el número de lanzamientos que desea: "))

historial = []

for i in range(1, lanzamientos + 1):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    
    historial.append((dado1, dado2))
    
    print(f"\nLanzamiento {i}: {nombre} lanzó {dado1} y {dado2}")
    
    if dado1 == dado2:
        print(f"¡Felicitaciones {nombre}! Puedes sacar una ficha ")

print("\nHistorial de lanzamientos")
for i, (d1, d2) in enumerate(historial, 1):
    print(f"  Lanzamiento {i}: {d1} y {d2}")
print("\n turno del siguiente jugador")
