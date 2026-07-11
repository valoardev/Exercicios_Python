# Faça um programa que calcule e exiba o fatorial de um número inteiro positivo n fornecido pelo
# usuário, utilizando um laço for.

n = int(input("Insira um número: "))

fatorial = 1
for i in range(n,0,-1):
    fatorial *= i

print(f"{n}! = {fatorial}")