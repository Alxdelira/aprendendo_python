numero = int(input('Valor para sacar: '))

cem = int(numero / 100)
numero = numero % 100
    
cinquenta = int(numero/50)
numero = numero % 50

dez = int(numero/10)
numero = numero % 10

cinco = int(numero/5)
numero = numero % 5

dois = int(numero/2)
numero = numero % 2

um = numero
    
print('Notas R$100,00 = {}'.format(cem))
print('Notas R$ 50,00 = {}'.format(cinquenta))
print('Notas R$ 10,00 = {}'.format(dez))
print('Notas R$  5,00 = {}'.format(cinco))
print('Notas R$  2,00 = {}'.format(dois))
print('Notas R$  1,00 = {}'.format(um))