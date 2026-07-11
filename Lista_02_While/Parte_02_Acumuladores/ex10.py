# Escreva um programa que leia um número inteiro positivo N e 
# calcule a soma de todos os números ímpares de 1 até N.

N = int(input("Insira um número: "))
inicio = 1
soma = 0
if N > 0:
    while inicio <= N:
        soma += inicio
        inicio += 2

    print(f"A soma de todos os número ímpares é: {soma}")
else:
    print("Digite um número inteiro positivo")