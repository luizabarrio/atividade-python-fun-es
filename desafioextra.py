def diferenca_maior_menor(numeros):
    maior = numeros[0]
    menor = numeros[0]

    for numero in numeros:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    return maior - menor


numeros = [5, 12, 8, 20, 3, 15, 7]

print("Diferença:", diferenca_maior_menor(numeros))