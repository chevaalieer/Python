import math

num = float(input("Informe um angulo: "))

seno = (math.sin(math.radians(num)))
print("O seno é: {:.2f}".format(seno))
tangente = (math.tan(math.radians(num)))
print("A Tangente é: {:.2f}".format(tangente))
cosseno = (math.cos(math.radians(num)))
print("O cosseno é: {:.2f}".format(cosseno))
