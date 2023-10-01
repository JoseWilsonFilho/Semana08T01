# Definição de função para calcularmos em dias a primeira data
def primeira_data(dia_01, mes_01, ano_01):
    primeira_data = (ano_01*365) + (mes_01*30) + dia_01
    return primeira_data

# Definição de função para calcularmos em dias a segunda data
def segunda_data(dia_02, mes_02, ano_02):
    segunda_data = (ano_02*365) + (mes_02*30) + dia_02
    return segunda_data

# Definição de função para calcularmos qual a data mais recente
def mais_recente(primeira_data, segunda_data):
    if primeira_data >= segunda_data:
        print(f'{dia_01}/{mes_01}/{ano_01}')
    elif primeira_data < segunda_data:
        print(f'{dia_02}/{mes_02}/{ano_02}')

# Definição das variáveis para a importação dos dados da primeira data do usuário
dia_01 = int(input())
mes_01 = int(input())
ano_01 = int(input())

# Definição das variáveis para a importação dos dados da segunda data do usuário
dia_02 = int(input())
mes_02 = int(input())
ano_02 = int(input())

# Chamar as funções da primeira e segunda data e definir a mais recente 
data_um = primeira_data(dia_01, mes_01, ano_01)
data_dois = segunda_data(dia_02, mes_02, ano_02)
data_mais_recente = mais_recente(data_um, data_dois)

    