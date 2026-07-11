# Escreva quatro funções: somar, subtrair, multiplicar e dividir. Cada uma recebe dois números (float) e
# retorna o resultado da operação correspondente. A função dividir deve retornar a string “Erro: divisão
# por zero” caso o divisor seja 0. No programa principal, leia dois números e um operador (+, -, *, /), use
# uma estrutura if/elif para chamar a função adequada e exiba o resultado.

def somar (numero1, numero2):
    return numero1 + numero2
def subtrair (numero1,numero2):
    return numero1 - numero2
def multiplicar (numero1, numero2):
    return numero1 * numero2
def dividir (numero1, numero2):
    if numero2 == 0:
        return "Erro: divisão por zero"    
    return numero1 / numero2

numero1 = float(input("Insira o valor do número 1: "))
while True:
    operador = input("Insira o operador (+, -, *, /): ")
    if operador in "+-*/":
        break
    print("Insira um operador válido!")
numero2 = float(input("Insira o valor do número 2: "))

if operador == "+":
    resultado = somar(numero1, numero2)
elif operador == "-":
    resultado = subtrair(numero1, numero2)
elif operador == "*":
    resultado = multiplicar(numero1, numero2)
else:
    resultado = dividir(numero1, numero2)
print(f"{numero1} {operador} {numero2} = {resultado}")