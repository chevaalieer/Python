# Solicita ao usuário que digite uma frase
frase_usuario = input("Digite uma frase: ")

# Remove os espaços da frase e converte para minúsculas
frase_formatada = frase_usuario.replace(" ", "").lower()

# Verifica se a frase formatada é um palíndromo
if frase_formatada == frase_formatada[::-1]:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
