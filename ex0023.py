'''numero = int(input("Digite um número: "))
numero_str = str(numero)
unidade = numero_str[3]
print("Unidade: {}".format(unidade))

dezena = numero_str[2]
print("Dezena: {}".format(dezena))

centena = numero_str[1]
print("Centena: {}".format(centena))

milhar = numero_str[0]
print("Milhar: {}".format(milhar))'''

num = float(input("Informe um número: "))
u = num // 1 % 10
print("Unidade: {:.0f}".format(u))
d = num // 10 % 10
print("Dezena: {:.0f}".format(d))
c = num // 100 % 10
print("Centena: {:.0f}".format(c))
m = num // 1000 % 10
print("Milhar: {:.0f}".format(m))