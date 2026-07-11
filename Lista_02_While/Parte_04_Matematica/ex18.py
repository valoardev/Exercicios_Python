# Escreva um programa que leia um número inteiro positivo e informe quantos dígitos ele possui. Utilize
# divisões sucessivas por 10

numero = int(input("Insira um número: "))
numero_inicio = numero
i = 0
if numero > 0:
    while numero != 0:
        numero = numero//10
        i += 1
    print(f"O número {numero_inicio} possui {i} dígitos")
elif numero == 0:
    print("O número que você inseriu é zero, é somente 1 dígito")
else:
    print("Insira um número positivo!")
