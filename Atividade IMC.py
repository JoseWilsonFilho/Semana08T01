# Definição da função para representar o IMC da pessoa
def imc (massa, altura):
    imc = massa / (altura ** 2)
    return imc

# Definição das variáveis para o usuário importar os dados de massa e altura
massa = float(input())
altura = float(input())
imc = imc(massa, altura)

# Definição das condições referente a classificação de IMC dadas na questão 
if imc < 18.5:
    print (f'{imc:.2f}')
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print (f'{imc:.2f}')
    print('Peso normal')
elif imc >= 25 and imc < 30:
    print (f'{imc:.2f}')
    print('Sobrepeso')
elif imc >= 30 and imc < 35:
    print (f'{imc:.2f}')
    print('Obeso leve')
elif imc >= 35 and imc < 40:
    print (f'{imc:.2f}')
    print('Obeso moderado')
elif imc >= 40:
    print (f'{imc:.2f}')
    print('Obeso mórbido')
