import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def pedir_valor():
    while True:
        try:
            valor = int(input("Ingresa la suma deseada (2-12): "))
            
            if valor < 2 or valor > 12:
                print("El número debe estar entre 2 y 12.")
            else:
                return valor
                
        except ValueError:
            print("Debes ingresar un número entero.")

def pedir_jugadores():
    while True:
        try:
            cantidad = int(input("¿Cuántos jugadores participarán? "))
            
            if cantidad <= 0:
                print("Debe ser un número mayor que 0.")
            else:
                return cantidad
                
        except ValueError:
            print("Debes ingresar un número entero.")

def intentos_hasta_objetivo(valor_objetivo):
    intentos = 0
    
    while True:
        intentos += 1
        dado1, dado2 = lanzar_dados()
        suma = dado1 + dado2
        
        print(f"Intento {intentos}: {dado1} + {dado2} = {suma}")
        
        if suma == valor_objetivo:
            return intentos, dado1, dado2

def jugar():
    print("\n===== LANZAMIENTO DE DADOS =====")
    
    cantidad_jugadores = pedir_jugadores()
    
    for i in range(cantidad_jugadores):
        print(f"\n--- Jugador {i+1} ---")
        
        nombre = input("Ingresa tu nombre: ")
        valor = pedir_valor()
        
        intentos, d1, d2 = intentos_hasta_objetivo(valor)
        
        print("\nRESULTADO FINAL")
        print(f"Jugador: {nombre}")
        print(f"Suma solicitada: {valor}")
        print(f"Combinación obtenida: {d1} + {d2} = {valor}")
        print(f"Intentos necesarios: {intentos}")

def main():
    while True:
        jugar()
        
        repetir = input("\n¿Desean jugar otra vez? (s/n): ").lower()
        if repetir != "s":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()
