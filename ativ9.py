def analisar_estoque(estoque):
    sem_estoque = 0
    estoque_baixo = 0
    estoque_normal = 0

    for quantidade in estoque:
        if quantidade == 0:
            sem_estoque += 1
        elif quantidade <= 3:
            estoque_baixo += 1
        else:
            estoque_normal += 1

    return sem_estoque, estoque_baixo, estoque_normal


estoque = [10, 3, 0, 7, 2, 15, 1, 0, 8]

sem, baixo, normal = analisar_estoque(estoque)

print("=== RELATÓRIO DE ESTOQUE ===")
print("Sem estoque:", sem)
print("Estoque baixo:", baixo)
print("Estoque normal:", normal)