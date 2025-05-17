#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Digite um ângulo: '))

#rad = ang * (math.pi / 180)
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print('O ângulo de {:.1f}º tem o seno de {:.2f}'.format(ang, sen))
print('O ângulo de {:.1f}º tem o cosseno de {:.2f}'.format(ang, cos))
print('O ângulo de {:.1f}º tem a tangente de {:.2f}'.format(ang, tan))
