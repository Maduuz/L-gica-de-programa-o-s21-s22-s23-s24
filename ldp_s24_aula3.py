# Simulação de dados de vendas diárias (produto, vendas diárias)
vendas_diarias = [
    ("Cheetos", 150),
    ("Fandangos", 200),
    ("Cheetos", 160),
    ("Doritos", 120),
    ("Fandangos", 180),
    ("Cheetos", 170),
    ("Doritos", 130),
    ("Fandangos", 210),
]

# Dicionário para armazenar o total de vendas
total_vendas = {}
dias_registrados = {}

# Processando os dados de vendas
for produto, venda in vendas_diarias:
    # Atualiza o total de vendas
    if produto not in total_vendas:
        total_vendas[produto] = 0
        dias_registrados[produto] = 0  # Inicializa contador de dias

    total_vendas[produto] += venda
    dias_registrados[produto] += 1  # Contando os dias de venda

# Calculando e exibindo os resultados
print("Relatório de Vendas:")
for produto, total in total_vendas.items():
    media_diaria = total / dias_registrados[produto]  # Calcula média
    print(f"{produto}: Total de vendas = {total}, Média diária = {media_diaria:.2f}")
