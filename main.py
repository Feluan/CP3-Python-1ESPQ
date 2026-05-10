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

# Verificação
if len(avaliacoes) == 0:
    print("\nNenhuma avaliação registrada.")
else:
    # Processamento
    soma = sum(avaliacoes)
    media = soma / len(avaliacoes)

    acima_80 = 0

    for nota in avaliacoes:
        if nota >= 80:
            acima_80 += 1

    # Saída
    print("\n=== RELATÓRIO JOVI ===")
    print(f"Total de avaliações: {len(avaliacoes)}")
    print(f"Média de qualidade: {media:.2f}")
    print(f"Avaliações acima de 80: {acima_80}")

    # Ordenação (extra - nível mais alto)
    avaliacoes.sort(reverse=True)
    print(f"Melhor avaliação: {avaliacoes[0]}")
    print(f"Pior avaliação: {avaliacoes[-1]}")

    print("\nHistórico (do melhor para o pior):")
    for nota in avaliacoes:
        print(f"- {nota}")
