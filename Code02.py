'''
Criar um programa em Python que receba como entrada quatro salarios. O programa dev calcular a media salarial e imprimir todos os salarios que estiverem abaixo da media
'''
salarios = [0, 0, 0, 0] #List
soma = 0
#Entrada
salarios[0] = float(input('Salario: R$'))
soma += salarios[0]
salarios[1] = float(input('Salario: R$'))
soma += salarios[1]
salarios[2] = float(input('Salario: R$'))
soma += salarios[2]
salarios[3] = float(input('Salario: R$'))
soma += salarios[3]

#Processamento
media = soma/4

print(f'Média: {media:.2f}')

#Saidas
if salarios[0] < media:
    print(f'Salario abaixo da média: {salarios[0]}')
if salarios[1] < media:
    print(f'Salario abaixo da média: {salarios[1]}')
if salarios[2] < media:
    print(f'Salario abaixo da média: {salarios[2]}')
if salarios[3] < media:
    print(f'Salario abaixo da média: {salarios[3]}')