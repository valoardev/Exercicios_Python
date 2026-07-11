# Escreva uma função chamada verificar_paridade que receba um número inteiro (int) e exiba na tela se
# ele é “par” ou “ímpar”. No programa principal, leia o número e chame a função

def verificar_paridade (numero):
    """
    Função que verifica se o número é impar ou par
    """
    if numero%2 == 0:
        print(f"O número {numero} é Par")
    else:
        print(f"O número {numero} é Ímpar")

numero = int(input("Insira um número: "))
verificar_paridade(numero)
        