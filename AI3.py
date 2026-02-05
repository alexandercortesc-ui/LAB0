import random

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
for _ in range(n_lanzamientos):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    lanzamientos.append((dado1, dado2))

    # Clasificación
    if dado1 == dado2:
        presadas += 1
    elif (dado1 == 5 and dado2 == 6) or (dado1 == 6 and dado2 == 5):
        cinco_seis += 1
    elif (dado1 == 1 and dado2 == 2) or (dado1 == 2 and dado2 == 1):
        pate_perro += 1

# Cálculo de porcentajes
porc_presadas = (presadas / n_lanzamientos) * 100
porc_cinco_seis = (cinco_seis / n_lanzamientos) * 100
porc_pate_perro = (pate_perro / n_lanzamientos) * 100

# Resultados
print(f"\nJugador: {jugador}")
print("Lanzamientos:", lanzamientos)

print("\nPorcentajes:")
print(f"Presadas: {porc_presadas:.2f}%")
print(f"5-6: {porc_cinco_seis:.2f}%")
print(f"Pate-perro (1-2): {porc_pate_perro:.2f}%")