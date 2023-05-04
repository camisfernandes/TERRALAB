#Exercicio 016- Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Exemplo: número = 6.172   parte inteira = 6

from math import trunc #importacao da biblioteca necessaria

numero = float(input('Digite um numero:'))

print('A parte inteira de {} = {}'.format(numero, trunc(numero))) #trunc pega a parte inteira automaticamente




