#Exercicio 005- Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.

n = int(input('Digite um número: '))

print('Antecessor de {}: {} \nSucessor de {}: {}'.format(n, (n - 1), n, (n + 1)))