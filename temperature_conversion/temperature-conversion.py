def line():
    print('-'*50)


def celsius():
    result = (temperature*1.8) + 32
    print(f'The temperature {temperature:.1f}°C converted is from {result:.1f}°F')


def fahrenheit():
    result = (temperature - 32) / 1.8
    print(f'The temperature {temperature:.1f}°F converted is from {result:.1f}°C')


def print_tabela():
    print(
    '''
    [1] Celsius(°C) to Fahrenheit(°F)
    [2] Fahrenheit(°F) to Celsius(°C)
    [3] to close the program
    '''
    )
    
while True:
    line()
    print('Which operation do you want to do?')
    line()
    print_tabela()
    line()

    option = int(input('Enter the option: '))
    if option == 1 or option == 2:
        line()
        temperature = float(input('Enter the temperature you want to convert: '))

        if option == 1:
            celsius()
        elif option == 2:
            fahrenheit()
    elif option == 3:
        print('Finishing..')
        break
    else:
        print('Invalid command. ERROR')