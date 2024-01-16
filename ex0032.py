
# Solicita ao usuário que insira um ano
ano_informado = int(input("Informe um ano: "))

# Verifica se o ano é bissexto e imprime o resultado
if (ano_informado % 4 == 0 and ano_informado % 100 != 0) or (ano_informado % 400 == 0):
    print(f"{ano_informado} é um ano bissexto.")
else:
    print(f"{ano_informado} não é um ano bissexto.")
