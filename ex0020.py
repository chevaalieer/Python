from random import shuffle

trab1 = (input("Informe o nome do trabalho1: "))
trab2 = (input("Informe o nome do trabalho2: "))
trab3 = (input("Informe o nome do trabalho3: "))
trab4 = (input("Informe o nome do trabalho4: "))
list_trab = [trab1, trab2, trab3, trab4]
shuffle(list_trab)
print(list_trab)
