# Função para validar e ler a nota
def ler_nota():
    while True:
        try:
            nota = float(input("Digite a nota: "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("nota inválida")
        except ValueError:
            print("nota inválida")

# Lê as duas notas válidas
nota1 = ler_nota()
nota2 = ler_nota()

# Calcula a média
media = (nota1 + nota2) / 2

# Imprime a média formatada
print(f"média = {media:.2f}")
