#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

v = float(input('Insira um valor em metros: '))

km = v / 1000
hm = v / 100
dam = v / 10
dm = v * 10
cm = v * 100
mm = v * 1000

print('A medida de {}m corresponde a:'.format(v))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))
