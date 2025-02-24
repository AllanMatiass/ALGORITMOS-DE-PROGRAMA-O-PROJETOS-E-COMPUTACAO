# Nota: as funções estão definidas apenas para controlar o fluxo de prints/inputs. (não ficar perguntando toda hora);


def beauty_print(msg:str):
    print('='*30)
    print(msg)
    print('='*30)



def fahreinheit_to_celsius():
    beauty_print('Convertendo de Fahrenheit para celsius')

    F = float(input('Digite a temperatura: '))
    C = (F - 32) * 5/9
    print(f'O resultado da conversão de {F} para celsius é: {C:.2f}\n')

# fahreinheit_to_celsius()

def dolar_exchange():
    beauty_print('Convertendo dolar para reais')

    brl_exchange = float(input('Digite a cotação atual do dólar: '))
    dolar_input = float(input('Digite o valor em dólar: '))
    results = brl_exchange * dolar_input
    print(f'O valor em reais é: {results:.2f}')
    
# dolar_exchange()

def kmh_to_meters():
    beauty_print('Convertendo km/h para metros')
    
    kmh = int(input('Digite um valor inteiro em KM/H: '))
    kmh_in_meters = kmh / 3.6
    print(f'{kmh}/h para metros é: {kmh_in_meters}')

# kmh_to_meters()

def plumber_salary():
    beauty_print('Verificando o salário de um encanador.')
    daily_reward = 30
    how_much_plumber_worked = int(input('Digite o numero de dias que o encanador trabalhou: '))
    total_reward = daily_reward * how_much_plumber_worked
    salary = total_reward - (total_reward * 0.08)
    
    print(f'Salário com IR descontado: {salary}')

# plumber_salary()

def staircase():
    beauty_print('Calculando a altura das escadas')
    stair_height = int(input('Digite a altura da escada (cm): '))
    user_objective = int(input('Digite qual a altura que você deseja chegar (cm): '))

    # somar tudo e dividir pela altura da escada
    final = int((user_objective + stair_height) // stair_height)
    print(f'Em {final} degraus você chega no seu objetivo de {user_objective}cm considerando que a altura da escada é {stair_height}cm ')

# staircase()

def fuel_calculation():
    beauty_print('Calculando o consumo de combustível')
    km_per_liter = 12
    time_of_travel = int(input('Digite o tempo gasto na viagem (segundos): '))
    avg_speed = int(input('Digite a velocidade média do veículo: '))
    
    distance = avg_speed * time_of_travel
    fuel_consum = distance / km_per_liter

    hours = time_of_travel // 3600
    minutes = (time_of_travel % 3600) // 60
    seconds = time_of_travel % 60

    time = f'{hours:02}:{minutes:02}:{seconds:02}'

    beauty_print(f'Details\n\tVelocidade média: {avg_speed}\n\tTempo gasto na viagem: {time}\n\tDistância: {distance} metros\n\tQuantidade de combustível consumido: {fuel_consum}L')

# fuel_calculation()


def calculate_price_of_an_area():
    beauty_print('Calculando preço do terreno')


    width = int(input('Digite a largura do terreno: '))
    length = int(input('Digite o comprimento do terreno: '))
    price = float(input('Digite o preço do metro de tela: '))

    perimeter = 2 * (width + length)
    cost = perimeter * price

    print(f'O custo para cercar o terreno é: {cost}')

# calculate_price_of_an_area()

def three_digits():
    digits = int(input('Digite um numero inteiro de 3 digitos: '))
    print(str(digits[:-1]))

three_digits()