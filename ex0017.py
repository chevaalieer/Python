from math import hypot

n1 = float(input("Digite um valor para o Cateto Oposto: "))
n2 = float(input("Digite um valor para o Cateto Adjacente: "))

comprimento = hypot(n1,n2)


print("O comprimento da Hipotenusa é: {:.2f}".format(comprimento))
