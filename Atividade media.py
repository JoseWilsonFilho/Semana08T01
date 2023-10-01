# Definição da função para calcularmos a media dos numeros inteiros
def media_numeros(numero_01, numero_02, numero_03, numero_04, numero_05):
    media = (numero_01 + numero_02 + numero_03 + numero_04 + numero_05)/5
    return media

# Definição das variáveis com a importação dos dados do usuário
numero_01 = float(input())
numero_02 = float(input())
numero_03 = float(input())
numero_04 = float(input())
numero_05 = float(input())

# Imprimir na tela a media dos numeros e o numero que for maior que a media
media = media_numeros(numero_01, numero_02, numero_03, numero_04, numero_05)
media_final = media
print(f'{media_final:.2f}')

# Definição das condições para o numero informado for maior que a media
if numero_01 > media_final:
    print(f'{numero_01:.2f}')
if numero_02 > media_final:
    print(f'{numero_02:.2f}')
if numero_03 > media_final:
    print(f'{numero_03:.2f}')
if numero_04 > media_final:
    print(f'{numero_04:.2f}')
if numero_05 > media_final:
    print(f'{numero_05:.2f}')