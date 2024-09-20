# Função para calcular o total de quartos disponíveis
def calcular_quartos_disponiveis(hotel):
    total_vazios = 0  # Inicializa o contador de quartos vazios

    # Percorrendo cada andar (sublista) da matriz
    for andar in hotel:
        # Contando o número de quartos vazios no andar
        quartos_vazios_no_andar = andar.count('vazio')
        
        # Somando os quartos vazios deste andar ao total
        total_vazios += quartos_vazios_no_andar

    return total_vazios  # Retorna o total de quartos disponíveis

# Exemplo de uso da função
# Matriz representando o hotel (cada sublista é um andar)
hotel = [
    ['ocupado', 'vazio', 'vazio', 'ocupado'],  # 2 quartos vazios no 1º andar
    ['vazio', 'ocupado', 'vazio', 'vazio'],    # 3 quartos vazios no 2º andar
    ['ocupado', 'ocupado', 'vazio', 'vazio']   # 2 quartos vazios no 3º andar
]

# Chamando a função para calcular os quartos disponíveis
total_quartos_vazios = calcular_quartos_disponiveis(hotel)

# Exibindo o total de quartos disponíveis
print(f"Total de quartos disponíveis: {total_quartos_vazios}")
