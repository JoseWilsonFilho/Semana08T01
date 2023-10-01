# Definição das variáveis dos 5 números que serão importados pelo usuário
numero_01 = int(input())
numero_02 = int(input())
numero_03 = int(input())
numero_04 = int(input())
numero_05 = int(input())

# Definição do maior e menor entre as variáveis 
numeros = [numero_01, numero_02, numero_03, numero_04, numero_05]
menor = numeros[0]
maior = numeros [0]
for numero_05 in numeros:
    if numero_05 < menor:
        menor = numero_05
    if numero_05 > maior:
        maior = numero_05

print(maior)
print(menor)

