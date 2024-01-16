from datetime import date

ano_nascimento = int(input("\nDigite seu ano de nascimento: "))
ano_atual = date.today().year - ano_nascimento

if ano_atual <= 9:
    print("\nSua categoria é: MIRIM")
elif ano_atual > 9 and ano_atual <= 14:
    print("\nSua categoria é: INFANTIL")
elif ano_atual > 14 and ano_atual <= 19:
    print("\nSua categoria é: JUNIOR")
elif ano_atual > 19 and ano_atual <= 20:
    print("\nSua categoria é: SÊNIOR")
else:
    print("\nSua categoria é: MASTER")