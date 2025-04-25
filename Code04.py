salarios = []
soma = 0

#Preencher [List]
for i in range(4):
    salario = float(input('Salario R$: '))
    salarios.append(salario)
    soma += salario

media = soma / len(salarios)

for salario in salarios:
    if salario < media:
        print(f'Salario abaixo da média:{salario:.2f}')    