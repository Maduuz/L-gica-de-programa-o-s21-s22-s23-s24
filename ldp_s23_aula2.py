def pode_tirar_ferias(tempo_servico, mes_ferias):
    # Define a temporada alta (dezembro, janeiro, fevereiro e julho)
    temporada_alta = ["dezembro", "janeiro", "fevereiro", "julho"]

    # Funcionários com mais de 3 anos de serviço podem tirar férias a qualquer momento
    if tempo_servico > 3:
        return True
    # Funcionários com 3 anos ou menos não podem tirar férias na temporada alta
    elif tempo_servico <= 3 and mes_ferias.lower() not in temporada_alta:
        return True
    else:
        return False

# Entrada de dados
tempo_servico = int(input("Digite o tempo de serviço do funcionário (em anos): "))
mes_ferias = input("Digite o mês em que o funcionário deseja tirar férias: ").strip()

# Verifica se o funcionário pode tirar férias
if pode_tirar_ferias(tempo_servico, mes_ferias):
    print("Pedido de férias aprovado.")
else:
    print("Pedido de férias negado.")
