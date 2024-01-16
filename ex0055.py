# Inicializa listas vazias para armazenar os pesos
pesos = []

# Loop para receber cinco entradas de peso
for _ in range(5):
    # Converte a entrada para um número de ponto flutuante e adiciona à lista
    peso = float(input("Digite seu peso: "))
    pesos.append(peso)

# Verifica o maior e o menor peso
maior_peso = max(pesos)
menor_peso = min(pesos)

# Exibe os resultados
print(f"\nO maior peso é: {maior_peso}")
print(f"O menor peso é: {menor_peso}")
