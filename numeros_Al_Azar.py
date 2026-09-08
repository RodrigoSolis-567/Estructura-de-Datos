import math
import random
from collections import Counter


def calcular_estadisticas():
  
    numeros = [random.randint(1, 100) for _ in range(50)]

    media = sum(numeros) / len(numeros)

    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)

    mediana = (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2

    conteo = Counter(numeros)
    max_frecuencia = max(conteo.values())

    if max_frecuencia > 1:
        moda = [num for num, freq in conteo.items() if freq == max_frecuencia]
    else:
        moda = "No hay moda (todos los números aparecieron una sola vez)"

    varianza = sum((x - media) ** 2 for x in numeros) / (n - 1)

    desviacion_estandar = math.sqrt(varianza)

    print("=== NÚMEROS GENERADOS ===")
    print(numeros)
    print("\n=== RESULTADOS ESTADÍSTICOS ===")
    print(f"Media: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Moda: {moda} (frecuencia: {max_frecuencia})")
    print(f"Varianza (muestral): {varianza:.2f}")
    print(f"Desviación estándar (muestral): {desviacion_estandar:.2f}")


calcular_estadisticas()