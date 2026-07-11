# Escreva uma função chamada maior que receba dois números inteiros (int) e retorne o maior deles. Se
# forem iguais, retorne qualquer um. No programa principal, leia dois números, chame a função e exiba
# o resultado

def maior (numero1, numero2):
    """
    Função que exibe qual é o maior número entre os inseridos
    """
    if numero1 > numero2:
        maior = numero1
    elif numero2 > numero1:
        maior = numero2
    else:
        maior=numero1
    return maior

numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira um número: "))
resultado = maior(numero1, numero2)
print(f"O maior número entre esses é o {resultado}")
