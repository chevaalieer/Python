# Solicita ao usuário que insira o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Inicializa uma lista para armazenar os 10 primeiros termos
termos_pa = []

# Calcula e armazena os 10 primeiros termos na lista
for i in range(10):
    termo_atual = primeiro_termo + i * razao
    termos_pa.append(termo_atual)

# Exibe os 10 primeiros termos da PA
print("Os 10 primeiros termos da PA são:")
for termo in termos_pa:
    print(termo)
