# Escreva um programa que leia um número inteiro positivo N e exiba a contagem regressiva de N até 0

N = int(input("Digite um número inteiro positivo:"))

if N>0:
    while N != 0:
        print(N)
        N -= 1
    print(0)
else:
    print("Insira um número positivo")