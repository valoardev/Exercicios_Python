# Escreva um programa que leia números inteiros positivos até que o usuário digite 0 (sentinela). Para
# cada número, o programa deve informar se ele é um palíndromo (ou seja, se o número lido de trás para
# frente é igual ao original). Ao final, exiba quantos palíndromos foram encontrados.

quantidade_palindromos = 0

numero = int(input("Digite um número inteiro positivo (0 para sair): "))

while numero != 0:
    original = numero
    invertido = 0

    while numero > 0:
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero //= 10

    if original == invertido:
        print(f"{original} é um palíndromo.")
        quantidade_palindromos += 1
    else:
        print(f"{original} não é um palíndromo.")

    numero = int(input("Digite um número inteiro positivo (0 para sair): "))

print(f"Foram encontrados {quantidade_palindromos} palíndromos.")
    