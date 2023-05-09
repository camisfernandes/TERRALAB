#Exercicio 094- Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostrei:
#A) quanras pessoas cadastradas
#B) a média de idade
#C) uma lista com mulheres
#D) uma lista com idade acima da média

pessoa = dict()
galera = list()
soma = media = 0


while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break

        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')

    if resp == 'N':
        break

print('-' * 50)

media = soma / len(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'A média de idade é de {media:5.2f} anos')

print('As mulheres cadastradas foram ', end = '')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end = '')

print()

print(f'Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v, in p.items():
            print(f'{k} = {v} ', end = ' ')
        print()



