def main():
    pares= [2,4,6,8,10]
    impares= [1,3,6,7,9]

    mostrarVector(pares)
    print("media= "+str(media(pares)))
    mostrarVector(impares)
    print("media= " +str(media(impares)))


def mostrarVector(datos):
    for i in range(len(datos)):
        print(datos[i])


def media(datos):
    n=len(datos)
    suma=0
    for i in range(n):
        suma = suma + datos[i]
    return suma / n

main()
        
    