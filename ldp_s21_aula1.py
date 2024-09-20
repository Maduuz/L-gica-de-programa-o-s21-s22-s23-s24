# Função para reorganizar a agenda dos artistas
def reorganizar_agenda(agenda, artista_cancelado, novo_artista):
    # Verificando se o artista cancelado está na agenda
    if artista_cancelado in agenda:
        # Encontrando o índice do artista cancelado
        indice = agenda.index(artista_cancelado)
        
        # Removendo o artista cancelado da lista
        agenda.pop(indice)
        
        # Inserindo o novo artista na mesma posição
        agenda.insert(indice, novo_artista)
        
        print(f"Artista '{artista_cancelado}' removido. Novo artista '{novo_artista}' adicionado na posição {indice}.")
    else:
        print(f"Artista '{artista_cancelado}' não encontrado na agenda.")

# Exemplo de uso da função
# Lista inicial de artistas na agenda
agenda_artistas = ["Taylor Swift", "Ariana Grande", "Lady Gaga", "The Weeknd"]

# Artista que cancelou a apresentação
artista_cancelado = "Ariana Grande"

# Novo artista que vai substituir o cancelado
novo_artista = "Sabrina Carpenter"

# Chamando a função para reorganizar a agenda
reorganizar_agenda(agenda_artistas, artista_cancelado, novo_artista)

# Exibindo a nova agenda
print("Nova agenda de artistas:", agenda_artistas)
