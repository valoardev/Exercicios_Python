# Escreva um programa que leia um valor N e 
# exiba todos os termos da sequência de Fibonacci menores que N

N = float(input("Insira o valor limite da sequência: "))
termo1 = 0
termo2 = 1
print(f"Sequência de Fibonacci até {N}:")
while termo1 + termo2 < N:
    print(F"{termo1} + {termo2} = {termo1+termo2}")
    temp = termo2 
    termo2 = termo1+termo2
    termo1 = temp 