# 1. Base de dados
equipe = [
    {"nome": "Ana", "tarefas": 12, "interacoes": 30},
    {"nome": "Bruno", "tarefas": 4, "interacoes": 15},
    {"nome": "Carla", "tarefas": 8, "interacoes": 22},
    {"nome": "Daniel", "tarefas": 2, "interacoes": 5},
    {"nome": "Elisa", "tarefas": 15, "interacoes": 40},
    {"nome": "Felipe", "tarefas": 6, "interacoes": 18},
    {"nome": "Gabriela", "tarefas": 10, "interacoes": 27},
    {"nome": "Henrique", "tarefas": 3, "interacoes": 9},
    {"nome": "Isabela", "tarefas": 14, "interacoes": 35},
    {"nome": "João", "tarefas": 7, "interacoes": 20}
]

# 2. Parâmetros do negócio
meta = 5

# 3. Contadores
count_alta = 0
count_media = 0
count_baixa = 0

print("\n=== ANÁLISE DE PERFORMANCE DA EQUIPE ===\n")

# 4. Loop principal
for pessoa in equipe:
    nome = pessoa["nome"]
    tarefas = pessoa["tarefas"]

    # Classificação de performance
    if tarefas >= 10:
        performance = "Alta"
        count_alta += 1
    elif tarefas >= meta:
        performance = "Média"
        count_media += 1
    else:
        performance = "Baixa"
        count_baixa += 1

    # Avaliação da meta
    if tarefas >= meta:
        status_meta = "Atingiu a meta"
    else:
        status_meta = "Não atingiu a meta"

    # Impressão individual
    print(nome, "-", performance, "-", status_meta)

# 5. Resumo final
total = count_alta + count_media + count_baixa

print("\n=== RESUMO FINAL ===")
print("Performance Alta:", count_alta)
print("Performance Média:", count_media)
print("Performance Baixa:", count_baixa)
print("Total de pessoas:", total)

# 6. Insight simples
print("\n=== INSIGHT ===")
if count_baixa > 0:
    print("Atenção: existem pessoas abaixo da performance esperada.")
else:
    print("Toda a equipe está performando acima do mínimo esperado.")