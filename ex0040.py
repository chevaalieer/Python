n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

nota_media = (n1 + n2) / 2

if nota_media < 5:
    print("\nSua média foi abaixo de 5, portanto você está REPROVADO!")
elif nota_media >= 7.0:
    print("\nSua média foi acima de 7, portanto você está APROVADO!")
elif 5.0 <= nota_media <= 6.9:
    print("\nSua média foi: {}, portanto você está de RECUPERAÇÃO!".format(nota_media))

input("\nBoas Festas!")
