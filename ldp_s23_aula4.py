def alocar_recursos(experiencia, tipo_apresentacao):
    recursos = {
        "novato": {
            "palestra": {"tempo": 30, "equipamento": "projetor", "sala": "Sala 1"},
            "workshop": {"tempo": 45, "equipamento": "lousa, projetor", "sala": "Sala 2"},
            "demonstracao": {"tempo": 20, "equipamento": "tela, projetor", "sala": "Sala 3"}
        },
        "experiente": {
            "palestra": {"tempo": 45, "equipamento": "projetor, microfone", "sala": "Sala 4"},
            "workshop": {"tempo": 60, "equipamento": "lousa, projetor, material", "sala": "Sala 5"},
            "demonstracao": {"tempo": 30, "equipamento": "tela, projetor", "sala": "Sala 6"}
        },
        "especialista": {
            "palestra": {"tempo": 60, "equipamento": "projetor, microfone, gravação", "sala": "Sala 7"},
            "workshop": {"tempo": 90, "equipamento": "lousa, projetor, material especial", "sala": "Sala 8"},
            "demonstracao": {"tempo": 45, "equipamento": "tela, projetor, equipamento especial", "sala": "Sala 9"}
        }
    }

    return recursos.get(experiencia.lower(), {}).get(tipo_apresentacao.lower(), None)

# Entrada de dados
experiencia = input("Digite o nível de experiência do palestrante (novato, experiente, especialista): ").strip()
tipo_apresentacao = input("Digite o tipo de apresentação (palestra, workshop, demonstração): ").strip()

# Alocar recursos
recursos_alocados = alocar_recursos(experiencia, tipo_apresentacao)

# Saída
if recursos_alocados:
    print(f"Recursos alocados:")
    print(f"Tempo de apresentação: {recursos_alocados['tempo']} minutos")
    print(f"Equipamento: {recursos_alocados['equipamento']}")
    print(f"Sala: {recursos_alocados['sala']}")
else:
    print("Experiência ou tipo de apresentação inválidos.")
