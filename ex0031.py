d = int(input("Quantos KMs de distância a viagem tem: "))
p =  d * 0.50
l = d * 0.45

if d <= 200:
    print("\nO preço para está viagem é: R${:.2f}!".format(p))
else:
    print("\nO preço para está viagem longa é: R${:.2f}!".format(l))

print("\nObrigado por voar conosco!")

input("\nPressione Enter para sair")