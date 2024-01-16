# Solicita ao usuário que informe seu salário
cor_vermelha = '\033[91m'
s = float(input("Informe seu salário: "))

# Define a primeira faixa percentual de aumento (superior de 10%)
superior1 = 10
# Calcula o aumento para a primeira faixa
a1 = (s / 100) * superior1
# Calcula o novo salário para a primeira faixa
novo_salario1 = s + a1

# Define a segunda faixa percentual de aumento (superior de 15%)
superior2 = 15
# Calcula o aumento para a segunda faixa
a2 = (s / 100) * superior2
# Calcula o novo salário para a segunda faixa
novo_salario2 = s + a2

# Verifica em qual faixa o salário se encaixa e imprime o novo salário correspondente
if s >= 1251:
    print(cor_vermelha + "Seu salário vai ser de: R${:.2f}".format(novo_salario1))
else:
    print("Seu salário vai ser de: R${:.2f}".format(novo_salario2))


