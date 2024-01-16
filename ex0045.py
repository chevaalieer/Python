from time import sleep
import random

while True:
    # Apresentação das opções para o usuário
    print('''\n- Digite 1 para PEDRA
              \n- Digite 2 para PAPEL
              \n- Digite 3 para TESOURA''')

    # Solicita ao usuário que faça uma escolha
    escolha_usuario = input("\nEscolha uma opção (1/2/3): ")

    # Define as opções possíveis
    opcoes = ["PEDRA", "PAPEL", "TESOURA"]

    # O computador faz uma escolha aleatória
    escolha_pc = random.choice(opcoes)

    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")
    sleep(1)
    print('-=-' * 20)

    # Exibe as escolhas feitas
    print("\nVocê escolheu:", opcoes[int(escolha_usuario) - 1])
    print("O PC escolheu:", escolha_pc)

    # Verifica o resultado do jogo e imprime o resultado
    if escolha_usuario == str(opcoes.index(escolha_pc) + 1):
        print("\nEmpate!")
    elif (
        (escolha_usuario == "1" and escolha_pc == "TESOURA") or
        (escolha_usuario == "2" and escolha_pc == "PEDRA") or
        (escolha_usuario == "3" and escolha_pc == "PAPEL")
    ):
        print("\nVocê venceu!")
    else:
        print("\nVocê perdeu!")

    jogar_novamente = input("\nDeseja jogar novamente? (S/N): ").upper()
    if jogar_novamente != 'S':
        break
