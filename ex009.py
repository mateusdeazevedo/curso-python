#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número para ver sua tabuada: '))
m = 1

print('_'*12)
print('')

for x in range(10):
    if m < 10:
        print('{} x {:2} = {}'.format(n, m, n * m))
    else:
        print('{} x {} = {}'.format(n, m, n * m))
    m += 1

print('_'*12)
