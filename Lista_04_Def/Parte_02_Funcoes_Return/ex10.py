# Escreva uma função chamada fatorial que receba um número inteiro não negativo (int) e retorne o
# valor de n! (n fatorial). Use um laço while dentro da função para calcular o resultado. No programa
# principal, leia o número, chame a função e exiba o resultado no formato “5! = 120”.

def fatorial (numero):
    """"
    Função que retorna o resultado do fatorial do número inserido
    """
    resultado = 1 
    while numero > 1:
        resultado *= numero
        numero -= 1
    return resultado

while True:
    numero = int(input("Insira um número para calcular o seu fatorial: "))
    if numero >= 0:
        break
    else: 
        print("O número inserido é um número negativo, insira, número positivo")

resultado = fatorial(numero)
print(f"{numero}! = {resultado}")


     