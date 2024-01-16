nome = input("Digite algo: ")
print(type(nome))
print("So tem espaços?",(nome.isspace()))
print("È um número?",(nome.isnumeric()))
print("È alfabético?",(nome.isalpha()))
print("Está em maiúsculas?",(nome.isupper()))
print("Está em minúsculas?",(nome.islower()))
print("Está capitalizada?", (nome.istitle()))

