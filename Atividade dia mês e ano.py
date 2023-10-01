# A função retorna a data atual transformada em dias.
def data_em_dias(dia, mes, ano):
    dias = (ano*365) + mes*(30.42) + dia
    
    return dias
# A função retorna a data atual e a data de nascimento trasnformada em anos.
def calcula_idade(dia, mes, ano, dia_nascimento, mes_nascimento, ano_nascimento):
    idade = (data_em_dias(dia, mes, ano) - data_em_dias(dia_nascimento, mes_nascimento, ano_nascimento))//365
   
    return int(idade)
# A função permite ao usuário importar os dados e imprime na tela a idade em anos. 
def main():
    dia_atual = int(input())
    mes_atual = int(input())
    ano_atual = int(input())

    dia_nascimento = int(input())
    mes_nascimento = int(input())
    ano_nascimento = int(input())

    print(calcula_idade(dia_atual, mes_atual, ano_atual, dia_nascimento, mes_nascimento, ano_nascimento))


if __name__ == '__main__':
    main()