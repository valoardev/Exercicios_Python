# Escreva as seguintes funções: (a) ler_nota, que receba uma mensagem (str) como parâmetro e retorne
# uma nota válida entre 0 e 10 (float), usando um laço while com try/except para validar a entrada; (b)
# calcular_media, que receba três notas (float) e retorne a média aritmética; (c) classificar, que receba a
# média (float) e retorne “Aprovado”, “Recuperação” ou “Reprovado” conforme as faixas ≥ 7, ≥ 5 ou <
# 5; (d) exibir_boletim, que receba nome (str), três notas e a situação (str) e exiba um boletim formatado.
# No programa principal, leia o nome do aluno, use ler_nota três vezes, calcule a média com
# calcular_media, classifique com classificar e exiba tudo com exibir_boletim.

def ler_nota (mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            print("Nota inválida!")
        except ValueError:
            print("Nota inválida!")

def calcular_media(nota1,nota2,nota3):
    return (nota1+nota2+nota3)/3

def classificar (media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    return "Reprovado"

def exibir_boletim(nome,nota1,nota2,nota3,situacao):
    print(f"""\n=== BOLETIM ===
Nome completo: {nome}
Primeira nota: {nota1:.2f}
Segunda nota: {nota2:.2f}
Terceira nota: {nota3:.2f}
Situação: {situacao}""")

nome = input("Insira o seu nome: ")       
nota1 = ler_nota("Digite a primeira nota: ")
nota2 = ler_nota("Digite a segunda nota: ")
nota3 = ler_nota("Digite a terceira nota: ")
media = calcular_media(nota1,nota2,nota3)
situacao = classificar(media)
exibir_boletim(nome,nota1,nota2,nota3,situacao)