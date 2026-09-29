def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# Genera los números
primeros_500 = fibonacci(100)

# Imprimir cada número con su índice
for idx, num in enumerate(primeros_500):
    print(f"F_{idx}: {num}")