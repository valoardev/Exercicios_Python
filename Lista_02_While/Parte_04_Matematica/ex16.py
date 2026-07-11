# Escreva um programa que leia um número inteiro não negativo N e calcule seu fatorial (N!) utilizando while.

numero = int(input("Insira um número: "))
i = 1
soma = 1
if numero > 0:
    while i <= numero:
        soma *= i
        i += 1
    print(f"O resultado do {numero} fatorial é: {soma}")
else:
    print("Insira um número positivo!")