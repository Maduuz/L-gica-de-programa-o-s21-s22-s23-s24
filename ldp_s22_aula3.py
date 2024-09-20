# Lê o número de casos de teste
N = int(input("Digite a quantidade de casos de teste: "))

# Loop para processar cada caso de teste
for _ in range(N):
    # Lê os valores X e Y
    X, Y = map(int, input("Digite os valores X e Y: ").split())
    
    # Garante que X seja o menor e Y o maior
    if X > Y:
        X, Y = Y, X

    # Inicializa a soma dos ímpares
    soma_impares = 0
    
    # Percorre os números entre X e Y
    for numero in range(X + 1, Y):  # Considera apenas os números entre X e Y
        if numero % 2 != 0:  # Verifica se o número é ímpar
            soma_impares += numero
    
    # Imprime a soma dos ímpares para o caso de teste
    print(f"Soma dos ímpares entre {X} e {Y}: {soma_impares}")