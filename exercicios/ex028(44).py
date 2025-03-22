print(f'{' Loja Gabriel ':=^40}')
preco=float(input('Preço das Compras R$'))
print ('''FORMA DE PAGAMENTO
    [ 1 ] à vista dinheiro/cheque
    [ 2 ] à vista cartao
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão
    Qual é a opção?''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    total = preco - (preco * 0.10)  
elif opcao == 2:
    total = preco - (preco * 0.05)  
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opcao == 4:
    total = preco + (preco * 0.20)  
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS')
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento')

print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')