# Escreva um programa que leia números inteiros até que o usuário digite 0 (sentinela). Ao final, exiba a
# soma de todos os valores lidos (excluindo o sentinela).

sentinela = 1
soma = 0
while sentinela != 0:
    numero = int(input("Insira um número: "))
    if numero == 0:
        print("Sentinela Ativado! Programa Interrompido")
        print(f"A soma de todos os valores inseridos é: {soma}")
        sentinela = 0
    else:
        soma += numero


    