print("{:=^40}".format("LOJAS CHEVALIER"))

preco_produto = float(input("Digite o preço do produto: "))

# Condição de Pagamento
print("\nEscolha uma condição de pagamento"
      "\n- Digite 1 para À vista dinheiro/cheque"
      "\n- Digite 2 para À vista no cartão"
      "\n- Digite 3 para até 2x no cartão"
      "\n- Digite 4 para 3x ou mais no cartão")

condicao = int(input("Escolha a condição de pagamento: "))

if condicao == 1:
    desconto = preco_produto * 0.10
    total_pagar = preco_produto - desconto
    print("\nÀ vista dinheiro/cheque com desconto de 10%. Total a pagar: R${:.2f}".format(total_pagar))
elif condicao == 2:
    desconto = preco_produto * 0.05
    total_pagar = preco_produto - desconto
    print("\nÀ vista no cartão com desconto de 5%. Total a pagar: R${:.2f}".format(total_pagar))
elif condicao == 3:
    total_pagar = preco_produto / 2
    print("\nAté 2x no cartão. Total a pagar: R${:.2f}".format(total_pagar))
elif condicao == 4:
    parcela = int(input("Em quantas parcelas você quer? "))
    juros = preco_produto * 0.20
    total_pagar = preco_produto + juros
    total_parcela = total_pagar / parcela  # Correção aqui
    print("\nVocê pagará no cartão em: {} Parcelas com 20% de juros. Total a pagar: R${:.2f} com parcelas de R${:.2f}".format(parcela, total_pagar, total_parcela))
else:
    print("\nOpção inválida. Por favor, escolha uma opção válida (1, 2, 3 ou 4).")
