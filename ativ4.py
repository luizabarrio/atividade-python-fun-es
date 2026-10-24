def analisar_numeros(numeros):
    positivos = 0
    negativos = 0
    zeros = 0

    for numero in numeros:
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            zeros += 1

    return positivos, negativos, zeros


numeros = [8, -3, 0, 12, -7, 5, 0, -1, 9, 4]

positivos, negativos, zeros = analisar_numeros(numeros)

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Zeros:", zeros)