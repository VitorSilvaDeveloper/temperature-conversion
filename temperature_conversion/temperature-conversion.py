def line():
    print('-'*50)


def celsius():
    result = (temperature*1.8) + 32
    print(f'The temperature {temperature:.1f}°C converted is from {result:.1f}°F')


def fahrenheit():
    result = (temperature - 32) / 1.8
    print(f'The temperature {temperature:.1f}°F converted is from {result:.1f}°C')

def kelvin_c():
    result = (temperature - 273.15)
    print(f'The temperature {temperature:.1f}K converted is from {result:.1f}°C')


def c_kelvin():
    result = (temperature + 273.15)
    print(f'The temperature {temperature:.1f}°C converted is from {result:.1f}k')


def fahrenheit_k():
    result = (temperature - 32) * 5/9 + 273.15
    print(f'The temperature {temperature:.1f}°F converted is from {result:.1f}k')

def k_fahrenheit():
    result = (temperature - 273.15) * 9/5 + 32
    print(f'The temperature {temperature:.1f}K converted is from {result:.1f}°F')

def print_tabela():
    print(
    '''
    [1] Celsius(°C) to Fahrenheit(°F)
    [2] Fahrenheit(°F) to Celsius(°C)
    [3] Kevin(K) to Celsius(°C)
    [4] Celsius(°C) to Kevin(K)
    [5] Fahrenheit(°F) to Kevin(K)
    [6] Kevin(K) to Fahrenheit(°F)
    [7] to close the program
    '''
    )
    
while True:
    line()
    print('Which operation do you want to do?')
    line()
    print_tabela()
    line()

    option = int(input('Enter the option: '))
    if option == 1 or option == 2 or option == 3 or option == 4 or option == 5 or option == 6:
        line()
        temperature = float(input('Enter the temperature you want to convert: '))

        if option == 1:
            celsius()
        elif option == 2:
            fahrenheit()
        elif option == 3:
            kelvin_c()
        elif option == 4:
            c_kelvin()
        elif option == 5:
            fahrenheit_k()
        elif option == 6:
            k_fahrenheit()
        else: 
            print('Invalid command. ERROR')
        
    elif option == 7:
        print('Finishing..')
        break
    else:
        print('Invalid command. ERROR')