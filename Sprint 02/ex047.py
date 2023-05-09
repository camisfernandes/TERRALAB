#Exercicio 047-  um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

#for n in range(1, 51):
#    if n % 2 == 0:
#        print(n, end = ' ')

#opcao 2
for n in range(2, 51, 2): #começa em 2, vai ate 51 e pula de 2 em 2
    print(n, end = ' ')