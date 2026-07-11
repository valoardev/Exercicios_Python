# Escreva um programa que leia números inteiros até que o usuário digite 999 (sentinela). Ao final,
# informe quantos valores positivos, negativos e zeros foram digitados

p = 0
n = 0
z = 0

numero = int(input("Insira um número inteiro: "))
if numero == 999:
    print("Você digitou o sentinela, nenhum número válido inserido")
else:
    while numero != 999:
        if numero > 0:
            p += 1
        elif numero < 0:
            n += 1
        else: 
            z += 1
        numero = int(input("Insira um número inteiro: "))

    print(f"Os números inseridos no seu programa estão classificados em: \n {p} positivos \n {n} negativos \n {z} zeros")
   
    

