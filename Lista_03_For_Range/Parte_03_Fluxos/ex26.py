# Utilizando for-else, escreva um programa que busque um valor em uma lista de números inteiros. Se o
# valor for encontrado, exiba sua posição (índice) e interrompa com break. Se não for encontrado, o
# bloco else deve informar que o valor não está na lista.
# Dica: combine enumerate() com for-else para obter o índice.

lista_numeros = [1,2,5,7,8,3,4,7,0,12,4,5,35,5,67,9,32,81]

n = int(input("Insira um número a ser procurado: "))

for indice, valor in enumerate(lista_numeros):
    if valor == n:
        print(f"Valor encontrado se encontra no índice {indice}")
        break
else:
    print("O valor não está na lista")