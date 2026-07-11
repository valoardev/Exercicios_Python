# Faça um programa que leia n notas de alunos (valores de 0 a 10) e exiba ao final: a média da turma, a
# maior nota e quantos alunos ficaram acima da média. Utilize um laço for com padrão acumulador e
# uma lista para armazenar as notas.

n = int(input("Quantos alunos a turma possui? "))
lista = []
maior_nota = 0
soma = 0
acima_media = 0
for i in range(1,n+1):
    nota = int(input(f"Insira a nota {i}: "))
    lista.append(nota)
    soma += nota
    if nota > maior_nota:
        maior_nota = nota
media = soma/n
for aluno in lista:
    if aluno > media:
        acima_media += 1
print(f"A maior nota da turma foi {maior_nota}")
print(f"A média das notas informadas é {media}")
print(f"{acima_media} alunos ficaram acima da média")


