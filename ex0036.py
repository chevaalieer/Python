# Empréstimo Bancário

valor_casa = float(input("Qual o valor da casa: "))
salario = float(input("Qual o valor do seu Salário: "))
quantos_anos = float(input("Em quantos anos você pretende pagar? "))

# Cálculo da Prestação
prestacao_mensal = valor_casa / (quantos_anos * 12)

print("\nVocê pagará o valor das prestações em: R${:.2f} por mês".format(prestacao_mensal))

# Condição Aninhada
limite_porcentagem = 30  # Limite de 30% do salário para o pagamento da prestação
limite_prestacao = (salario * limite_porcentagem) / 100

if prestacao_mensal <= limite_prestacao:
    print("\nSeu empréstimo foi aprovado!")
else:
    print("\nSeu empréstimo foi negado!")
    print("O valor da prestação excede 30% do seu salário.")
