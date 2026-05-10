# JOVI Academy - Controle de Avaliações de Tradução

print("=== JOVI Academy Mode ===")
print("Registro de avaliações da qualidade da tradução (0 a 100)\n")

avaliacoes = []

# Entrada de dados
while True:
    entrada = input("Digite uma avaliação (ou 'sair' para finalizar): ")

    if entrada.lower() == "sair":
        break

    try:
        nota = int(entrada)

        if 0 <= nota <= 100:
            avaliacoes.append(nota)
        else:
            print("Digite um valor entre 0 e 100.")
    except:
        print("Entrada inválida. Digite um número.")
