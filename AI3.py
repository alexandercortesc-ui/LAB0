import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

# Solicitar datos al usuario
jugador = input("Ingrese el nombre del jugador: ")
n_lanzamientos = int(input("Ingrese el número de lanzamientos: "))

# Lista para almacenar los lanzamientos
lanzamientos = []

# Contadores de categorías
presadas = 0
cinco_seis = 0
pate_perro = 0

# Simulación de los lanzamientos
for i in range(1, n_lanzamientos + 1):
    dado1, dado2 = lanzar_dados()
    lanzamientos.append((dado1, dado2))

    print(f"\nLanzamiento {i}: {jugador} lanzó {dado1} y {dado2}")

    # Clasificación
    if dado1 == dado2:
        presadas += 1
        print(f"¡Felicitaciones {jugador}! Puedes sacar una ficha")
    elif (dado1 == 5 and dado2 == 6) or (dado1 == 6 and dado2 == 5):
        cinco_seis += 1
    elif (dado1 == 1 and dado2 == 2) or (dado1 == 2 and dado2 == 1):
        pate_perro += 1

# Historial
print("\nHistorial de lanzamientos:")
for i in range(1, n_lanzamientos + 1):
    d1, d2 = lanzamientos[i - 1]
    print(f"  Lanzamiento {i}: {d1} y {d2}")

# Cálculo de porcentajes
porc_presadas = (presadas / n_lanzamientos) * 100
porc_cinco_seis = (cinco_seis / n_lanzamientos) * 100
porc_pate_perro = (pate_perro / n_lanzamientos) * 100

# Resultados
print(f"\nJugador: {jugador}")
print(f"Lanzamientos: {n_lanzamientos}")

print("\nPorcentajes:")
print(f"  Presadas:          {porc_presadas:.2f}%")
print(f"  5-6:               {porc_cinco_seis:.2f}%")
print(f"  Pate-perro (1-2):  {porc_pate_perro:.2f}%")
