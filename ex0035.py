#A Desigualdade Triangular afirma que a soma de quaisquer dois lados de um triângulo deve ser sempre maior que o comprimento do terceiro lado

print('-=-'*20)
print('Analisador de triângulos')
print('-=-'*20)
r1 = float(input("Digite o comprimeiro de uma reta: "))
r2 = float(input("Digite o comprimeiro da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Podem formar um triângulo!")
else:
    print("Não podem formar um triângulo!")