#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc

n = float(input('Digite um valor: '))

p = trunc(n)

'''O trunc serve para pegar a porção inteira de um número real, porém o floor também serve, 
já que ele arredonda os números para baixo.'''

print('A porção inteira do número {} é {}.'.format(n, p))
