#Exercicio 065- Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = 'S'
media = quantidade = soma = maior = menor = 0

while continuar in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade+= 1

    if numero > maior:
        maior = numero

    if numero < maior:
        menor = numero




    continuar = str(input('Continuar? [S/N]: ')).upper().strip()[0]

media = soma / quantidade


print('Media dos numeros digitados = {} \n'.format(media))
print('Maior valor digitado: {}\nMenor valor digitado: {}'.format(maior, menor))
