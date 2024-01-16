import random

num = int(input("Vou pensar em um número entre 0 e 5. Tente Adivinhar... \n"))
num_escolhido = random.randint(0,5)

print("\nEm que Nùmero eu pensei?")
print('-=-' * 20)
print("\nPROCESSANDO...")

print('-=-' * 20)

if num == num_escolhido:
    print("\nVocê venceu!")
else:
    print("\nVocê perdeu!")

print('-=-' * 20)

print("\nO Número escolhido era: {}".format(num_escolhido))
