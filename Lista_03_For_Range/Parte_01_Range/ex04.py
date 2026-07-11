# Escreva um programa que leia um número inteiro n do usuário e 
# exiba a tabuada desse número (de 1 a 10), no formato n x i = resultado

N = int(input("Insira um número: "))

print(f"Tabuada do {N}:")
for i in range(1,11):
    N*i
    print(f"{N} x {i} = {N*i}")

