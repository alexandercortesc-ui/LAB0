import random

nombre = input("Ingrese el nombre del jugador: ")
lanzamientos = int(input("Seleccione el número de lanzamientos que desea: "))

historial_dado1 = []
historial_dado2 = []

for i in range(1, lanzamientos + 1):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    historial_dado1.append(dado1)
    historial_dado2.append(dado2)

    print(f"\nLanzamiento {i}: {nombre} lanzó {dado1} y {dado2}")

    if dado1 == dado2:
        print(f"¡Felicitaciones {nombre}! Puedes sacar una ficha")

print("\nHistorial de lanzamientos:")
for i in range(lanzamientos):
    print(f"  Lanzamiento {i + 1}: {historial_dado1[i]} y {historial_dado2[i]}")

presadas = 0
cinco_seis = 0
pate_perro = 0

for i in range(lanzamientos):
    d1 = historial_dado1[i]
    d2 = historial_dado2[i]

    if d1 == d2:
        presadas += 1
    elif (d1 == 5 and d2 == 6) or (d1 == 6 and d2 == 5):
        cinco_seis += 1
    elif (d1 == 1 and d2 == 2) or (d1 == 2 and d2 == 1):
        pate_perro += 1

porc_presadas = (presadas / lanzamientos) * 100
porc_cinco_seis = (cinco_seis / lanzamientos) * 100
porc_pate_perro = (pate_perro / lanzamientos) * 100

ultimo_d1 = historial_dado1[lanzamientos - 1]
ultimo_d2 = historial_dado2[lanzamientos - 1]

print(f"\nJugador: {nombre}")
print(f"Lanzamientos: {lanzamientos}")

print("\nPorcentajes:")
print(f"  Presadas:          {porc_presadas:.2f}%")
print(f"  5-6:               {porc_cinco_seis:.2f}%")
print(f"  Pate-perro (1-2):  {porc_pate_perro:.2f}%")
print(f"El número de casillas a avanzar para el jugador {nombre} es de {ultimo_d1 + ultimo_d2}")