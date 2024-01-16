'''n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 >= n2 and n1 >= n3:
    print("O maior número é {:.0f}".format(n1))
elif n2 >= n1 and n2 >= n3:
    print("O maior número é {:.0f}".format(n2))
else:
    print("O maior número é {:.0f}".format(n3))

if n1 <= n2 and n1 <= n3:
    print("O menor número é {:.0f}".format(n1))
elif n2 <= n1 and n2 <= n3:
    print("O menor número é {:.0f}".format(n2))
else:
    print("O menor número é {:.0f}".format(n3))'''

# Solicita ao usuário que insira três números
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# Determina o maior número usando a função max()
maior_numero = max(n1, n2, n3)

# Determina o menor número usando a função min()
menor_numero = min(n1, n2, n3)

# Imprime o maior número formatado
print("O maior número é {:.0f}".format(maior_numero))

# Imprime o menor número formatado
print("O menor número é {:.0f}".format(menor_numero))
