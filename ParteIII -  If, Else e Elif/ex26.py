# Calculadora simples. Leia dois números e um operador (+, -, *, /). Exiba o resultado da operação.
# Trate a divisão por zero e operador inválido

numero1 = float(input("Insira o número:"))
numero2 = float(input("Insira o segundo número:"))
operador = input("Insira um operador: [+][-][x][/]:")

if operador == "+":
    resultado = numero1 + numero2
    print(f"O resultado da soma é: {resultado}")
elif operador == "-":
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif operador == "x":
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
elif operador == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operador inválido. Insira um operado válido: [+][-][x][/]")