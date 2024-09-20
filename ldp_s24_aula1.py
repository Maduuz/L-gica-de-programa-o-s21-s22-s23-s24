# Simulação de uma base de dados de bugs reportados
bugs_reportados = [
    {"id": 1, "gravidade": "alta", "descricao": "Erro na autenticação", "contagem": 8},
    {"id": 2, "gravidade": "media", "descricao": "Erro ao salvar o formulário", "contagem": 3},
    {"id": 3, "gravidade": "baixa", "descricao": "Texto de aviso incorreto", "contagem": 6},
    {"id": 4, "gravidade": "alta", "descricao": "Crash ao fechar o aplicativo", "contagem": 12},
    {"id": 5, "gravidade": "media", "descricao": "Problema de layout em tela", "contagem": 5},
    {"id": 6, "gravidade": "alta", "descricao": "Erro na integração com API", "contagem": 10},
    {"id": 7, "gravidade": "baixa", "descricao": "Link quebrado na página", "contagem": 2},
]

# Função para gerar o relatório de bugs
def gerar_relatorio(bugs):
    relatorio = {}
    
    # Processando bugs
    for bug in bugs:
        gravidade = bug["gravidade"]
        descricao = bug["descricao"]
        contagem = bug["contagem"]

        # Inicializando o dicionário para cada gravidade
        if gravidade not in relatorio:
            relatorio[gravidade] = []

        # Adicionando o bug ao relatório
        relatorio[gravidade].append({"descricao": descricao, "contagem": contagem})

    return relatorio

# Função para identificar bugs prioritários
def bugs_prioritarios(bugs):
    prioritarios = []
    for bug in bugs:
        if bug["contagem"] > 5:
            prioritarios.append(bug)
    return prioritarios

# Gerando o relatório
relatorio = gerar_relatorio(bugs_reportados)
prioritarios = bugs_prioritarios(bugs_reportados)

# Exibindo o relatório
print("Relatório de Bugs por Gravidade:\n")
for gravidade, bugs in relatorio.items():
    print(f"Gravidade: {gravidade}")
    for bug in bugs:
        print(f"  - {bug['descricao']}: {bug['contagem']} reportagens")
    print()

# Exibindo os bugs prioritários
print("Bugs Prioritários (mais de 5 reportagens):\n")
if prioritarios:
    for bug in prioritarios:
        print(f"- {bug['descricao']}: {bug['contagem']} reportagens")
else:
    print("Nenhum bug prioritário encontrado.")
