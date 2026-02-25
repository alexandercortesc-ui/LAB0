import random
import time
from collections import Counter

def validar_suma(suma_deseada):
    """Valida que la suma esté en el rango permitido."""
    if not 1 <= suma_deseada <= 12:
        raise ValueError("❌ Error: La suma debe estar entre 1 y 12.")

def intentos_hasta_suma_deseada(suma_deseada, verbose=False, delay=0):
    """
    Recibe un número entre 1 y 12.
    Lanza dos dados hasta obtener esa suma.
    Retorna la cantidad de intentos necesarios y el historial de resultados.
    
    Parámetros:
    - suma_deseada: número a buscar
    - verbose: si es True, muestra cada lanzamiento
    - delay: pausa entre lanzamientos (en segundos)
    """
    validar_suma(suma_deseada)
    
    intentos = 0
    historial = []
    
    while True:
        intentos += 1
        
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        
        historial.append((dado1, dado2, suma))
        
        if verbose:
            print(f"Intento #{intentos:3d}: 🎲 {dado1} + 🎲 {dado2} = {suma}")
            if delay > 0:
                time.sleep(delay)
        
        if suma == suma_deseada:
            if verbose:
                print(f"🎉 ¡Éxito en el intento #{intentos}!")
            return intentos, historial

def mostrar_estadisticas(historial, suma_deseada):
    """Muestra estadísticas de los lanzamientos."""
    total_intentos = len(historial)
    sumas = [suma for _, _, suma in historial]
    
    print(f"\n📊 Estadísticas de los {total_intentos} lanzamientos:")
    print(f"   • Suma más común: {Counter(sumas).most_common(1)[0][0]}")
    print(f"   • Suma promedio: {sum(sumas)/total_intentos:.2f}")
    print(f"   • Suma mínima: {min(sumas)}")
    print(f"   • Suma máxima: {max(sumas)}")
    
    # Probabilidad teórica vs real
    prob_teorica = calcular_probabilidad_teorica(suma_deseada)
    prob_real = 1/total_intentos
    
    print(f"\n📈 Probabilidad de obtener {suma_deseada}:")
    print(f"   • Teórica: {prob_teorica:.2%}")
    print(f"   • Real en este experimento: {prob_real:.2%}")

def calcular_probabilidad_teorica(suma):
    """Calcula la probabilidad teórica de obtener una suma con dos dados."""
    combinaciones = {
        2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6,
        8: 5, 9: 4, 10: 3, 11: 2, 12: 1
    }
    return combinaciones.get(suma, 0) / 36

def main():
    """Función principal del programa."""
    print("🎲 SIMULADOR DE LANZAMIENTO DE DADOS 🎲")
    print("=" * 40)
    
    while True:
        try:
            entrada = input("\nIngrese la suma deseada (1-12) o 'q' para salir: ")
            
            if entrada.lower() == 'q':
                print("👋 ¡Hasta luego!")
                break
            
            numero = int(entrada)
            
            # Preguntar por modo verbose
            verbose = input("¿Ver cada lanzamiento? (s/n): ").lower() == 's'
            
            if verbose:
                delay = float(input("Pausa entre lanzamientos (segundos, ej: 0.5): ") or 0)
            else:
                delay = 0
            
            print(f"\n🎯 Buscando suma {numero}...")
            inicio = time.time()
            
            intentos, historial = intentos_hasta_suma_deseada(numero, verbose, delay)
            
            tiempo_total = time.time() - inicio
            
            print(f"\n✅ RESULTADO: Se necesitaron {intentos} lanzamientos.")
            print(f"⏱️  Tiempo total: {tiempo_total:.2f} segundos")
            
            # Mostrar estadísticas
            mostrar_estadisticas(historial, numero)
            
            # Preguntar si quiere ver el resumen de sumas
            if input("\n📋 ¿Ver resumen de sumas obtenidas? (s/n): ").lower() == 's':
                print("\n📊 Frecuencia de sumas:")
                sumas_obtenidas = [suma for _, _, suma in historial]
                for suma in range(2, 13):
                    count = sumas_obtenidas.count(suma)
                    porcentaje = (count/len(historial))*100
                    barra = "█" * int(porcentaje/2)
                    print(f"   {suma:2d}: {barra:20} {count:3d} veces ({porcentaje:.1f}%)")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()