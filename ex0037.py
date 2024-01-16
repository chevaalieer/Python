# Início
num = int(input("Digite um número: "))
print("-=-" * 20)

# Método de Conversão
metodo_conversao = int(input("Escolha o tipo de conversão:\n"
                              "- 1 para binário\n"
                              "- 2 para octal\n"
                              "- 3 para hexadecimal\n"))

# Estrutura Aninhada
if metodo_conversao == 1:
    print("\nA representação de {} em binário é: {}".format(num, bin(num)[2:]))
elif metodo_conversao == 2:
    print("\nA representação de {} em octal é: {}".format(num, oct(num)[2:]))
elif metodo_conversao == 3:
    print("\nA representação de {} em hexadecimal é: {}".format(num, hex(num)[2:]))
else:
    print("\nDigite uma opção válida!")
