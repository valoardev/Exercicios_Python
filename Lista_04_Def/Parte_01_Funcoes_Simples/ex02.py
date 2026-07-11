# Escreva uma função chamada exibir_dobro que receba um número inteiro (int) como parâmetro e
# exiba na tela o dobro desse número. No programa principal, leia um inteiro via input() e chame a
# função.

def exibir_dobro (numero):
    """
    Função para exibir o dobro de um número informado
    """
    print(f"O dobro de {numero} é {numero*2:.0f}")

numero_inserido = int(input("Insira um número: "))
exibir_dobro(numero_inserido)
