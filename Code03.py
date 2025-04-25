'''
Criar um programa em Python que receba como entrada quatro salarios. O programa dev calcular a media salarial e imprimir todos os salarios que estiverem abaixo da media
'''
salarios = [0, 0, 0, 0] 
soma = 0

i = 0
while i < len(salarios):
    salarios[i] = float(input('Salario R$: '))
    soma += salarios[i]
    i+=1

media = soma / len(salarios)

print(f'Média: {media:.2f}')

i = 0
while i<len(salarios):
    if salarios[i] < media:
        print(f'Salarios abaixo da média: {salarios[i]:.2f}')
    i+=1


