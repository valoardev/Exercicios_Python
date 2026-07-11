# Escreva um programa que exiba a seguinte pirâmide centralizada, onde n é fornecido pelo usuário:
#     *
#    ***
#   *****
#  *******
# *********

n = int(input("Quantas linhas deve possuir a pirâmide: "))

for i in range(1,n+1):
    linha = "*" * (2*i - 1)
    espaco = " " * (n - i)
    print(espaco + linha)