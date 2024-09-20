# Simulação de dados de vendas mensais para produtos
vendas = {
    "Snickers": [150, 160, 170, 180, 190, 200],
    "Salgadinho": [200, 195, 190, 185, 180, 175],
    "Bolacha": [100, 110, 115, 120, 125, 130],
    "Ferrero Rocher": [300, 290, 280, 270, 260, 250],
}

# Inicializando listas para armazenar tendências
aumento_continuo = []
queda_continua = []

# Analisando vendas mês a mês
for produto, dados_venda in vendas.items():
    aumento = True
    queda = True

    for i in range(1, len(dados_venda)):
        if dados_venda[i] <= dados_venda[i - 1]:
            aumento = False
        if dados_venda[i] >= dados_venda[i - 1]:
            queda = False

    if aumento:
        aumento_continuo.append(produto)
    elif queda:
        queda_continua.append(produto)

# Exibindo os resultados
print("Produtos com aumento contínuo nas vendas:")
for produto in aumento_continuo:
    print(f"- {produto}")

print("\nProdutos com queda contínua nas vendas:")
for produto in queda_continua:
    print(f"- {produto}")
