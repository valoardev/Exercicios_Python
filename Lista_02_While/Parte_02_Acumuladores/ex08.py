# Escreva um programa que leia uma sequência de números inteiros positivos até que o usuário digite 0.
# Ao final, exiba o maior e o menor valor informado

# Escreva um programa que leia uma sequência de números inteiros positivos
# até que o usuário digite 0.
# Ao final, exiba o maior e o menor valor informado.

numero = int(input("Insira um número: "))

if numero == 0:
    print("Você digitou o sentinela, sem números válidos inseridos")
else:
    menor = numero
    maior = numero

    while numero != 0:
        numero = int(input("Insira um número: "))

        if numero > 0:
            if numero < menor:
                menor = numero

            if numero > maior:
                maior = numero

        elif numero < 0:
            print("Número inválido! Digite um número inteiro positivo.")

    print(f"O menor número inserido é: {menor}")
    print(f"O maior número inserido é: {maior}")

            
        

            

