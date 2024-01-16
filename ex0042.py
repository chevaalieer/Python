print("Analisador de Triângulos")
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

# Verifica se os lados formam um triângulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("\nOs lados informados podem formar um triângulo!")

    # Verifica o tipo de triângulo
    if lado1 == lado2 == lado3:
        print("\nEste é um triângulo Equilátero (todos os lados são iguais)")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("\nEste é um triângulo Isósceles (dois lados são iguais).")
    else:
        print("\nEste é um triângulo Escaleno (todos os lados são diferentes)")
else:
    print("\nOs lados informados não podem formar um triângulo.")
