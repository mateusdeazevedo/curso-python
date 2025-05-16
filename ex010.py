#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Cotação hoje (15/05/2025): U$D 1,00 = BRL R$ = 5,68

d = float(input('Quanto dinheiro você tem na carteira? R$'))

print('Com R${:.2f} você pode comprar US${:.2f}'.format(d, d / 5.68))
