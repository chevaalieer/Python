peso = float(input("\nDigite seu peso: "))
altura = float(input("\nDigite sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("\nAbaixo do peso")
elif 18.5 <= imc <= 25:
    print("\nPeso ideal")
elif 25 < imc <= 30:
    print("\nSobrepeso")
elif 30 < imc <= 40:
    print("\nObesidade")
else:
    print("\nObesidade mórbida")
