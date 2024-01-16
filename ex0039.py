from datetime import date

ano_nascimento = int(input("Digite o ano que você nasceu: "))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento

if idade < 18:
    print("\nVocê ainda vai se alistar")
    print("\nAinda faltam exatamente: {} anos para você se alistar".format(18 - idade))
elif idade == 18:
    print("\nJá é hora de você se alistar")
else:
    print("\nJá passou do tempo de você se alistar")
    print("\nJá se passaram exatamente: {} anos do limite".format(idade - 18))

