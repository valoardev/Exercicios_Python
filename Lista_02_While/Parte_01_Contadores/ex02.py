# Escreva um programa que leia dois números inteiros A e B (A < B) e 
# exiba todos os números pares existentes no intervalo [A, B]

A = int(input("Insira o valor de A: "))
B=  int(input("Insira o valor de B: "))

if A > B:
    print("Insira um número para que A seja menor que B")
while A <= B:
    if A%2 == 0:
        print(A)
        A += 2
    else:
        A += 1
        print(A)
        A += 1



