#Crie um programa que leia dois números inteiros e mostre a soma entre eles.

def soma(numero1, numero2):
    return numero1 + numero2

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print("{} + {} = {}".format(numero1, numero2, soma(numero1, numero2)))
