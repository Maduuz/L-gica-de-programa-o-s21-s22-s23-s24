# Inicializa contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Lê cinco valores inteiros
for _ in range(5):
    valor = int(input("Digite um valor inteiro: "))
    
    # Verifica se o valor é par ou ímpar
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Verifica se o valor é positivo ou negativo
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

# Imprime os resultados
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")