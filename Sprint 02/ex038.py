#Exercicio 038- Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#- o primeiro valor é maior
#- o segundo valor é maior
#- não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('\nO primeiro valor digitado é maior.')

elif n2 > n1:
    print('\nO segundo valor digitado é maior.')

else:
    print('\nOs dois valores digitados são iguais.')


