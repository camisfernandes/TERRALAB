#Exercicio 081- Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) quantos números foram digitados
#B) a lista de valores, ordenada de forma decrescente
#C) Se o valor 5 foi digitado e está ou não na lista

lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Continuar? [S/N] '))

    if continuar in 'Nn':
        break
print('-' * 30)
print(f'Quantidade de valores digitados: {len(lista)}')

lista.sort(reverse = True)
print(f'Valores em ordem decrescente: {lista}')

if 5 in lista:
    print('O valor 5 faz parte dos valores que foram digitados.')

else:
    print('O valor 5 não foi digitado.')




