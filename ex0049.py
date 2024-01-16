num = int(input("Digite um número para a tabuada: "))

print(f"\nTabuada do {num}:")

for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
