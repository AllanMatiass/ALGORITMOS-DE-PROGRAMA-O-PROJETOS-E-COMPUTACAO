
#Elabore um programa que leia um número inteiro e
# imprima o seu antecessor e o seu sucessor
try:
    number = int(input('Digite o número, irei dizer o antecessor e o sucessor: '))
    print(f'O antecessor de [{number}]  é {number - 1} \nO Sucessor de [{number}] é {number + 1}')
except ValueError:
    print('Digite apenas numeros;')

# Elabore um programa que dado o lado de um quadrado
# determine a sua área e seu perímetro

square = 5
perimetro = 4 * square
area = square**2

# area
print(f'A área de {square} é: {area}² ou {area}')

# perimetro
print('O perímetro de', square, 'é:', perimetro)


# Elabore um programa que imprima a parte inteira e o
# resto da divisão de dois números inteiros

number_one = float(input('Digite um número para dividir: '))
number_two = float(input('Digite outro número para ser o dividendo: '))

if (number_one == 0 or number_two == 0):
    print('não é possível dividir por 0')
    exit()

result = (number_one // number_two)
rest_result = (number_one % number_two)

print('Parte inteira da divisão:', result)

print()
print('Resto da divisão', rest_result)