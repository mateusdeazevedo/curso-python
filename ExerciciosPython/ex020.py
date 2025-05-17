#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

alunos = [input('Digite o nome do primeiro aluno: '), input('Digite o nome do segundo aluno: '),
          input('Digite o nome do terceiro aluno: '), input('Digite o nome do quarto aluno: ')]

shuffle(alunos)

print('Ordem sorteada: {}'.format(alunos))
