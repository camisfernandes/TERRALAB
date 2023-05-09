#Exercicio 052- Faça um programa que leia um número inteiro e diga se ele é ou nao um número primo.

numero = int(input('Digite um numero: '))
primo = 0

for cont in range(1, numero + 1):
    if numero % cont == 0:
        primo += 1


if primo == 2:
    print('O numero {} é primo.'.format(numero))

else:
    print('O numero {} não é primo.'.format(numero))