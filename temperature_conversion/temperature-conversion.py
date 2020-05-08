def linha():
    print('-'*50)


def celsius():
    resultado = (temperatura*1.8) + 32
    print(f'A temperatura {temperatura:.1f}°C convertida é de {resultado:.1f}°F')


def fahrenheit():
    resultado = (temperatura - 32) / 1.8
    print(f'A temperatura {temperatura:.1f}°F convertida é de {resultado:.1f}°C')


def print_tabela():
    print(
    '''
    [1] Celsius(°C) para Fahrenheit(°F)
    [2] Fahrenheit(°F) para Celsius(°C)
    [3] para encerrar o programa
    '''
    )
    
while True:
    linha()
    print('Qual operação deseja fazer?')
    linha()
    print_tabela()
    linha()

    opcao = int(input('Digite a opção: '))
    if opcao == 1 or opcao == 2:
        linha()
        temperatura = float(input('Digite a temperatura que quer converter: '))

        if opcao == 1:
            celsius()
        elif opcao == 2:
            fahrenheit()
    elif opcao == 3:
        print('Finalizando..')
        break
    else:
        print('Comando invalido. ERROR')