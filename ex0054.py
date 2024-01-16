from datetime import datetime

# Obtém o ano atual
ano_atual = datetime.now().year

# Idade mínima para atingir a maioridade
maioridade = 18

# Contadores para pessoas menores e maiores
pessoas_menores = 0
pessoas_maiores = 0

# Loop para obter o ano de nascimento de sete pessoas
for _ in range(7):
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    idade = ano_atual - ano_nascimento

    # Verifica se a pessoa é menor ou maior de idade
    if idade < maioridade:
        pessoas_menores += 1
    else:
        pessoas_maiores += 1

# Exibe o resultado
print("\nResultado:")
print(f"Pessoas menores de {maioridade} anos: {pessoas_menores}")
print(f"Pessoas maiores de {maioridade} anos: {pessoas_maiores}")
