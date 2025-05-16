#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

tempC = float(input('Informe a temperatura em ºC: '))

tempF = (tempC * 1.8) + 32

print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF.'.format(tempC, tempF))
