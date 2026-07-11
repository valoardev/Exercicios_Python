# Escreva uma função chamada situacao_aluno que receba duas notas (float) e retorne uma string:
# “Aprovado” se a média for maior ou igual a 7, “Recuperação” se for maior ou igual a 5, ou
# “Reprovado” caso contrário. No programa principal, leia as notas, chame a função e exiba o nome do
# aluno junto com sua situação

def situacao_aluno (nota1, nota2):
    """
    Função que calcula a média das notas do aluno e retorna situação atual
    """
    media = (nota1+nota2)/2
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

nome = (input("Insira seu nome: "))
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
situacao = situacao_aluno(nota1, nota2)

print(f"Querido aluno {nome}, sua situação é: {situacao}")