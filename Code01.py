'''
Criar um programa em Python que receba como entrada quatro salarios. O programa dev calcular a media salarial e imprimir todos os salarios que estiverem abaixo da media
'''

soma = 0
#Entrada
salario_1 = float(input('Salario: R$'))
soma += salario_1
salario_2 = float(input('Salario: R$'))
soma += salario_2
salario_3 = float(input('Salario: R$'))
soma += salario_3
salario_4 = float(input('Salario: R$'))
soma += salario_4

#Processamento
media = soma/4

print(f'Média: {media:.2f}')

#Salarios < Média
if salario_1 < media:
    print(f'Salario abaixo da média: {salario_1}')
if salario_2 < media:
    print(f'Salario abaixo da média: {salario_2}')
if salario_3 < media:
    print(f'Salario abaixo da média: {salario_3}')
if salario_4 < media:
    print(f'Salario abaixo da média: {salario_4}')          