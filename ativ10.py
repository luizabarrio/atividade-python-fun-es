def calcular_total(vendas):
    total = 0
    for venda in vendas:
        total += venda
    return total


def calcular_media_vendas(vendas):
    total = calcular_total(vendas)
    return total / len(vendas)


def maior_venda(vendas):
    maior = vendas[0]

    for venda in vendas:
        if venda > maior:
            maior = venda

    return maior


def contar_acima_media(vendas, media):
    quantidade = 0

    for venda in vendas:
        if venda > media:
            quantidade += 1

    return quantidade


vendas = [150, 300, 80, 500, 120, 450, 0, 200]

total = calcular_total(vendas)
media = calcular_media_vendas(vendas)
maior = maior_venda(vendas)
quantidade = contar_acima_media(vendas, media)

print("=== RELATÓRIO DE VENDAS ===")
print("Total vendido: R$", total)
print("Média das vendas: R$", round(media, 2))
print("Maior venda: R$", maior)
print("Vendas acima da média:", quantidade)