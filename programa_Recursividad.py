#recursividad anidada
def calcular_descuento_real(unidades, descuento_acumulado=0):
    if unidades < 100:
        return descuento_acumulado
    
    # Recursividad simple: un solo nivel de llamada
    return calcular_descuento_real(unidades - 100, descuento_acumulado + 5)

unidades = 500
descuento = calcular_descuento_real(unidades)

print(f"Venta de {unidades} unidades, descuento del {descuento}%") # Resultado: 25%