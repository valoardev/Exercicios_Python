# Escreva um programa que leia n números inteiros e conte separadamente quantos são positivos,
# negativos e iguais a zero.

n = int(input("Quantos números serão digitados? "))

positivos = 0
negativos = 0
zero = 0

for i in range(n):
    numero = int(input("Digite um número: "))

    if numero > 0:
        positivos += 1
        print("Número positivo")

    elif numero < 0:
        negativos += 1
        print("Número negativo")

    else:
        zero += 1
        print("Número igual a zero")

print(f"Quantidade de positivos: {positivos}")
print(f"Quantidade de negativos: {negativos}")
print(f"Quantidade de zeros: {zero}")