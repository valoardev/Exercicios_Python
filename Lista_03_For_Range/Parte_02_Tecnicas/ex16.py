# Escreva um programa que gere e exiba os n primeiros termos da sequência de Fibonacci (0, 1, 1, 2, 3,
# 5, 8, 13, ...) utilizando um laço for.

a = 0
b = 1 
limite = int(input("Digite o número limite da sequência: "))

for i in range(limite):
    print(a, end=", ")
    temp = a
    a=b
    b+=temp

    
