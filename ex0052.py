# Solicita ao usuário que insira um número
numero_inserido = int(input("Digite um número inteiro para verificar se é primo: "))

# Verifica se o número é menor que 2 (números menores que 2 não são primos)
if numero_inserido < 2:
    print(f"{numero_inserido} não é um número primo.")
else:
    # Verifica se o número é divisível por algum inteiro no intervalo de 2 até a raiz quadrada do número
    for i in range(2, int(numero_inserido**0.5) + 1):
        if numero_inserido % i == 0:
            print(f"{numero_inserido} não é um número primo.")
            break
    else:
        # Se não foi encontrado nenhum divisor, o número é primo
        print(f"{numero_inserido} é um número primo.")
