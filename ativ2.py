def calcular_situacao(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3

    if media < 5:
        situacao = "Reprovado"
    elif media < 7:
        situacao = "Recuperação"
    else:
        situacao = "Aprovado"

    return media, situacao


nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media, situacao = calcular_situacao(nota1, nota2, nota3)

print("Média:", media)
print("Situação:", situacao)