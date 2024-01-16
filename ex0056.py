# Inicializa listas e variáveis
nomes = []
idades = []
sexos = []

# Coleta de dados para 4 pessoas
for _ in range(4):
    print("\nDigite os dados da próxima pessoa:\n")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()

    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

# Calcula a média de idade
media_idade = sum(idades) / len(idades)

# Encontra o nome do homem mais velho (se houver homens)
homens = [(nome, idade) for nome, idade, sexo in zip(nomes, idades, sexos) if sexo == 'M']
nome_homem_mais_velho = max(homens, default=("", 0), key=lambda x: x[1])[0]

# Conta mulheres com menos de 20 anos
mulheres_menos_20 = sum(1 for idade, sexo in zip(idades, sexos) if sexo == 'F' and idade < 20)

# Exibe os resultados
print(f"\nA média de idade do grupo é: {media_idade:.2f}")
print(f"O homem mais velho é: {nome_homem_mais_velho}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")
