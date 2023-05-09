#Exercicio 078- Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = list()
maior = menor = 0

for i in range(0, 5):
    lista.append(int(input('Posicao {}: '.format(i + 1))))

    if i == 0:
        maior = menor = lista[i]

    else:
        if lista[i] > maior:
            maior = lista[i]

            if lista[i] < menor:
                menor = lista[i]

print(f'Valores digitados: {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end = '')

for i, v in enumerate(lista):
    if v == maior:
        print(f'{i} ', end = ' ')

print(f'\nO menor valor digitado foi {menor} nas posições ', end = '')

for i, v in enumerate(lista):
    if v == menor:
        print(f'{i} ', end = '')


