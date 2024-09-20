# Versão revisada do código que tem no AVA
def pode_acessar(cargo, dia_semana):
    dias_uteis = {"segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"}
    
    # Converter para minúsculas para comparação
    cargo = cargo.lower()
    dia_semana = dia_semana.lower()

    # Gerentes têm acesso irrestrito
    if cargo == "gerente":
        return True
    # Analistas e estagiários têm acesso somente em dias úteis
    elif cargo in {"analista", "estagiário"} and dia_semana in dias_uteis:
        return True

    return False

# Teste do programa
cargo = input("Digite o cargo do funcionário: ").strip()
dia_semana = input("Digite o dia da semana: ").strip()

if pode_acessar(cargo, dia_semana):
    print("Acesso Permitido.")
else:
    print("Acesso Negado.")
