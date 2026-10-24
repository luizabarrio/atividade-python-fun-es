def media_acima_limite(valores, limite):
    soma = 0
    quantidade = 0

    for valor in valores:
        if valor > limite:
            soma += valor
            quantidade += 1

    if quantidade == 0:
        return 0

    return soma / quantidade


valores = [20, 50, 80, 10, 100, 60, 25]
print("Média:", media_acima_limite(valores, 40))