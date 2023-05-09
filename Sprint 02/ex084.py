#Exercicio 084- Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
#A) quantas pessoas foram cadastradas
#B) uma listagem com as pessoas mais pesadas
#C) uma listagem com as pessoas mais leves

temporaria = list()
principal = list()
maior = menor = 0

while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))

    if len(principal) == 0:
        maior = menor = temporaria[1]

    else:
        if temporaria[1] > maior:
            maior = temporaria[1]

        if temporaria[1] < menor:
            menor = temporaria[1]

    principal.append(temporaria[:])
    temporaria.clear()
    continuar = str(input('Deseja continuar? [S/N] '))

    if continuar in 'Nn':
        break


print('-' * 50)
#quantidade de pessoas cadastradas
print(f'Quantidade de pessoas cadastradas: {len(principal)}')
print(f'Maior peso: {maior}kg')
print('Pesos de: ')
for pessoa in principal:
    if pessoa[1] == maior:
        print(f'{pessoa[0]}')

print(f'\nMenor peso: {menor}kg')
print('Pesos de: ')
for pessoa in principal:
    if pessoa[1] == menor:
        print(f'{pessoa[0]}')



