# Escreva uma função chamada saudacao que receba um nome (str) como parâmetro e exiba na tela a
# mensagem “Olá, [nome]! Seja bem-vindo(a) ao Python.”. No programa principal, peça ao usuário que
# digite seu nome e chame a função

def saudacao (nome):
    """
    Exibe uma mensagem de boas-vindas com o nome informado
    """
    print(f"Olá, {nome}! Seja bem-vindo(a) ao Python")

nome_usuario = input("Digite o seu nome: ")

saudacao(nome_usuario)