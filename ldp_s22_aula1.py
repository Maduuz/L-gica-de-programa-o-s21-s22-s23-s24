# Lê os dados de entrada
numero_funcionario = int(input("Número do funcionário: "))
horas_trabalhadas = int(input("Horas trabalhadas: "))
valor_por_hora = float(input("Valor por hora: "))

# Calcula o salário
salario = horas_trabalhadas * valor_por_hora

# Imprime o resultado formatado
print(f"Número = {numero_funcionario}")
print(f"Salário = $ {salario:.2f}")
