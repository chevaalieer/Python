# Inicializa a variável para armazenar a soma
soma_pares = 0

# Loop para ler seis números inteiros
for i in range(6):
    numero = int(input(f'Digite o {i + 1}º número inteiro: '))

    # Verifica se o número é par
    if numero % 2 == 0:
        soma_pares += numero

# Mostra a soma dos números pares
print(f'A soma dos números pares é: {soma_pares}')
