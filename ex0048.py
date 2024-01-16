resultado = 0
cont = 0

for soma in range(1, 501, 2):
    if soma % 3 == 0:
        resultado += soma
        cont = cont + 1

print(f"A soma de todos os {cont} valores é: {resultado}")
