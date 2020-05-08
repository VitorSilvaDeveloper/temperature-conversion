def linha():
    print('-'*50)

print('Qual operação deseja fazer?')
linha()
print(
    '''
    [1] Celsius(°C) para Fahrenheit(°F)
    [2] Fahrenheit(°F) para Celsius(°C)
    '''
)
linha()
opcao = int(input('Digite a opção: '))
linha()

def convertendo():
    if opcao == 1:
        temperatura = float(input('Digite a temperatura que quer converter: ')) 
        resultado = (temperatura*1.8) + 32
        print(f'A temperatura {temperatura:.1f}°C convertida é de {resultado:.1f}°F')
    elif opcao == 2:
        temperatura = float(input('Digite a temperatura que quer converter: '))
        resultado = (temperatura - 32) /1.8
        print(f'A temperatura {temperatura:.1f}°C convertida é de {resultado:.1f}°F')
convertendo()