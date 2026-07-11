# Escreva um programa que leia dois números inteiros positivos e calcule o Máximo Divisor Comum
# (MDC) entre eles utilizando o algoritmo de Euclides

numero1 = int(input("Insira o primeiro número: "))
numero2 = int(input("Insira o segundo número: "))

if numero1 > numero2 and numero2 != 0 and numero1 != 0:
    resto = numero1%numero2
    while resto != 0:
        numero1 = numero2
        numero2 = resto
        resto = numero1%numero2
    print(f"O Máximo Divisor Comum é {numero2}")
elif numero1 == 0:
    print(f"O primeiro número não pode ser igual a zero")
elif numero2 == 0:
    print(f"O segundo número não pode ser igual a zero")
else:
    print(f"o primeiro número deve ser maior que o segundo! {numero1} é menor que {numero2}")
            