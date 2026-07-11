# Escreva um programa que leia notas de alunos (entre 0 e 10) até que seja digitado um valor negativo
# (sentinela). Ao final, exiba a quantidade de notas lidas e a média aritmética

sentinela = 1
i = 0
soma = 0
while sentinela > 0:
    nota = float(input("Insira a nota do aluno: "))
    if nota < 0:
        if i > 0:
            print("Sentinela Ativado! Programa Encerrado")
            print(f"Foram lidas {i} notas")
            print(f"A média aritmética é: {soma/i}")
        else:
            print("Nenhuma nota válida foi inserida")
        sentinela = 0
    elif nota > 10:
        print("Insira um valor entre 0 e 10 para continuar")
    else:
        i += 1
        soma += nota



