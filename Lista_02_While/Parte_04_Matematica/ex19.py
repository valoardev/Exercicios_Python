# Escreva um programa que leia um número inteiro positivo e calcule a soma de seus dígitos

numero = int(input("Insira um número: "))
numero_inicio = numero
soma = 0
if numero >= 0:
    while numero != 0:
        digito = numero%10
        soma += digito
        numero = numero//10
    print(f"A soma dos dígitos do número {numero_inicio} é {soma}")
else:
    print("Insira um número positivo!!")