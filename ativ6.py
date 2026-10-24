def segundo_maior(numeros):
    maior = numeros[0]
    segundo = None

    for numero in numeros:
        if numero > maior:
            segundo = maior
            maior = numero
        elif numero < maior:
            if segundo is None or numero > segundo:
                segundo = numero

    return segundo


numeros = [15, 8, 22, 10, 30, 18]
print("Segundo maior número:", segundo_maior(numeros))