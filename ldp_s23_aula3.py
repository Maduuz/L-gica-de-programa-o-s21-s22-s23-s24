def classificar_produto(preco, categoria):
    # Definindo as faixas de preços para cada categoria
    if categoria.lower() == "luxo":
        if preco > 1000:
            return "Premium"
        else:
            return "Padrão"
    elif categoria.lower() == "moda":
        if preco < 100:
            return "Acessível"
        elif 100 <= preco <= 500:
            return "Padrão"
        else:
            return "Premium"
    elif categoria.lower() == "eletrônicos":
        if preco < 300:
            return "Acessível"
        elif 300 <= preco <= 1000:
            return "Padrão"
        else:
            return "Premium"
    else:
        return "Categoria desconhecida"

# Entrada de dados
preco = float(input("Digite o preço do produto: "))
categoria = input("Digite a categoria do produto (luxo, moda, eletrônicos): ").strip()

# Classificação do produto
classificacao = classificar_produto(preco, categoria)

# Saída
print(f"A classificação do produto é: {classificacao}")


