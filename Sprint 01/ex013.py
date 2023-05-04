#Exercicio 013- Faça um algoritmo que leia o salário de seu funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salario: '))
aumento = (salario * 15) / 100

print('Novo salario: R${:.2f}'.format(salario + aumento))