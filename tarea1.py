import random

def lanzar_dados():
    
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    return dado1, dado2, suma

def verificar_presadas(dado1, dado2):
    
    return dado1 == dado2

def main():
    
    # Solicitar nombre del jugador
    nombre = input("Por favor, introduce tu nombre: ")
    
    # Confirmar inicio del turno
    input(f"\nTurno de {nombre}. Presiona Enter para lanzar los dados...")
    
    # Lanzar los dados
    dado1, dado2, suma = lanzar_dados()
    
    # Mostrar resultados
    print(f"\nResultado del lanzamiento:")
    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    print(f"Suma: {suma}")
    
    # Verificar si obtuvo presadas y mostrar el mensaje correspondiente
    if verificar_presadas(dado1, dado2):
        print(f"\n¡Felicitaciones {nombre}! Puedes sacar una ficha")
    else:
        print(f"\nTurno del siguiente jugador")

if __name__ == "__main__":
    main()