import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

nombre = input("Ingrese el nombre del jugador: ")
lanzamientos = int(input("Seleccione el número de lanzamientos que desea: "))

historial = []

for i in range(1, lanzamientos + 1):
    dado1, dado2 = lanzar_dados()

    historial.append((dado1, dado2))

    print(f"\nLanzamiento {i}: {nombre} lanzó {dado1} y {dado2}")

    if dado1 == dado2:
        print(f"¡Felicitaciones {nombre}! Puedes sacar una ficha")

print("\nHistorial de lanzamientos:")
for i in range(1, lanzamientos + 1):
    d1, d2 = historial[i - 1]
    print(f"  Lanzamiento {i}: {d1} y {d2}")

presadas = 0
cinco_seis = 0
pate_perro = 0

for d1, d2 in historial:
    if d1 == d2:
        presadas += 1
    elif (d1 == 5 and d2 == 6) or (d1 == 6 and d2 == 5):
        cinco_seis += 1
    elif (d1 == 1 and d2 == 2) or (d1 == 2 and d2 == 1):
        pate_perro += 1

porc_presadas = (presadas / lanzamientos) * 100
porc_cinco_seis = (cinco_seis / lanzamientos) * 100
porc_pate_perro = (pate_perro / lanzamientos) * 100

ultimo_d1, ultimo_d2 = historial[-1]

print(f"\nJugador: {nombre}")
print(f"Lanzamientos: {lanzamientos}")

print("\nPorcentajes:")
print(f"  Presadas:          {porc_presadas:.2f}%")
print(f"  5-6:               {porc_cinco_seis:.2f}%")
print(f"  Pate-perro (1-2):  {porc_pate_perro:.2f}%")
print(f"El número de casillas a avanzar para el jugador {nombre} es de {ultimo_d1 + ultimo_d2}")
