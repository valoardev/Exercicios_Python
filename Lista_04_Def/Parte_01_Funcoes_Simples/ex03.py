# Escreva uma função chamada ficha_cadastral que receba três parâmetros: nome (str), idade (int) e
# altura (float). A função deve exibir os dados formatados, mostrando a altura com duas casas decimais.
# No programa principal, leia os três dados e chame a função

def ficha_cadastral (nome, idade, altura):
    """
    Exibe a mensagem da ficha cadastral do usuário formatada
    """
    print(f"=== Ficha Cadastral === \nNome: {nome} \nIdade: {idade} anos \nAltura: {altura:.2f} m")

nome = str(input("Insira seu nome: "))
idade = int(input("Insira sua idade: "))
altura = float(input("Insira sua altura: "))
ficha_cadastral(nome, idade, altura)