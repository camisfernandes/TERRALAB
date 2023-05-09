#Exercico 053- Crie um programa que leoa uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper()

#separar palavras da frase
palavras = frase.split()

#juntar palavras sem espaço
junto = ''.join(palavras)

#criando a string inversa
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print('O inverso de {} é {}: '.format(junto, inverso))

if inverso == junto:
    print('A frase digitada é um palíndromo.')

else:
    print('A frase digitada não é um palíndromo.')
