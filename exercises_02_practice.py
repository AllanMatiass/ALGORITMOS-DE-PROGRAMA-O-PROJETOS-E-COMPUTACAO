#Leia um número inteiro e imprima resultado da diferença do seu
# triplo pelo dobro do seu sucessor

number = float(input('Digite um numero: '))
number_times_three = number * 3
sucessor_times_two = (number + 1) * 2
difference = number_times_three - sucessor_times_two
print('Diferença:', difference)

#Determine a área de um triângulo
base = 10
altura = 5

area = (base * altura) / 2
print('A area do triangulo é:', area)

# Leia o salário mensal atual de um funcionário e o percentual de
# reajuste e determine o valor do novo salário

salary = float(input('Digite seu salario: '))
percentual = float(input('Digite o percentual de reajuste: '))
new_salary = salary * (1 + percentual / 100)
print(f'O novo salário será: {new_salary:.2f}')

# Calcule o volume do cubo

side = float(input('Digite o comprimento do lado do cubo: '))
volume = side ** 3
print(f'O volume do cubo é {volume}')

# labore um programa que dada uma distância percorrida (em
# quilômetros), bem como o total de combustível gasto (em litros),
# informe o consumo do veículo

distance = float(input('Digite a distancia (KM): '))
fuel_losed = float(input('Digite o combustivel gasto (L): '))
print(f'O consumo do veículo é: {distance / fuel_losed}')

# Faça um programa que dadas as medidas de uma sala em metro
# (comprimento e largura), bem como o preço do metro quadrado
# do carpete, informe o custo total para forrar o piso da sala

comprimento = float(input('Digite o comprimento: '))
largura = float(input('Digite a largura: '))
metro_carpete = float(input('Digite o preço do metro do carpete: '))
area = comprimento * largura
custo_total = area * metro_carpete
print(f'A area da sala é {area:.2f} m²')
print(f'O custo total para forrar é: R${custo_total:.2f}')

#  índice de massa corpórea (IMC) de uma pessoa é igual ao peso
# (em quilogramas) dividido pelo quadrado de sua altura (em
# metros). Construa um programa que dados o peso e altura de
# uma pessoa, informe o valor de seu IMC

peso = float(input('Digite o peso: '))
altura_ao_quadrado = float(input('Digite sua altura: ')) ** 2
results = peso * altura_ao_quadrado
print(f'O IMC é: {results}')