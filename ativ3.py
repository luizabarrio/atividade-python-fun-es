def calcular_compra(valor):
    if valor < 100:
        desconto = 0
    elif valor < 300:
        desconto = 0.05
    elif valor < 500:
        desconto = 0.10
    else:
        desconto = 0.15

    return valor * (1 - desconto)


valor = float(input("Valor da compra: R$ "))

valor_final = calcular_compra(valor)

print("Valor original: R$", valor)
print("Valor final: R$", round(valor_final, 2))
print("Valor economizado: R$", round(valor - valor_final, 2))