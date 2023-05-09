#Exercicio 042- Refaça o DESAFIO 035, acrescentando o recurso de mostrar que tipo de triângulo será formado
#- equilatero: todos os lados iguais
#- isosceles: dois lados iguais
#- escaleno: todos os lados diferentes

lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos digitados podem formar um triangulo ', end = '')
    if(lado1 == lado2 == lado3):
        print('EQUILATERO.')

    elif lado1 != lado2 != lado3 != lado1:
        print('ESCALENO.')

    else:
        print('ISOSCELES.')

else:
    print('Os segmentos digitados não podem formar um triangulo.')


