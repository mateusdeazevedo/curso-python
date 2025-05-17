#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

#Método que gasta muitas linhas:
'''
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

alunoEscolhido = choice(alunos)

print('O aluno escolhido para apagar o quadro foi o {}.'.format(alunoEscolhido))
'''
#Método que economiza linhas
alunos = [input('Digite o nome do primeiro aluno: '), input('Digite o nome do segundo aluno: '),
          input('Digite o nome do terceiro aluno: '), input('Digite o nome do quarto aluno: ')]

print('O aluno escolhido para apagar o quadro foi o {}.'.format(choice(alunos)))
