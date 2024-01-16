frase = input("Digite uma frase: ").upper().strip()
print("A letra A aparece: {}".format(frase.count("A")))
print("Ela aparece na posição pela primeira vez: {}".format(frase.find("A")))
print("Ela aparece pela ultima vez na posição: {}".format(frase.rfind("A")))
