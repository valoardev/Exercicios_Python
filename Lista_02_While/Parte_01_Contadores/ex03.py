# Escreva um programa que leia um número inteiro e exiba sua tabuada de multiplicação de 1 a 10.

numero = int(input("Insira um número inteiro: "))

print("Tabuada:")
x=1 
while x <= 10:
    print(f"{numero}x{x} = {numero*x}")
    x+=1
