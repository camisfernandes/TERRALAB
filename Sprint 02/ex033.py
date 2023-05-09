#Exercicio 033- Faça um programa que leia três número e mostre qual deles é o maior e qual deles é o menor

n1 = int(input('Digite o primeiro numero:'))
n2= int(input('Digite o segundo numero:'))
n3 = int(input('Digite o terceiro numero:'))

#verificando o menor numero
menor = n1

if n2 <n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3

#verificando o maior numero
maior = n1

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3

#impressao dos valores
print('Menor valor digitado: {}\nMaior valor digitado: {}'.format(menor, maior))

