# Escreva um programa que leia dois números e exiba a divisão do primeiro pelo segundo. Caso o
# segundo número seja zero, o programa deve solicitar um novo valor para o divisor até que ele seja
# diferente de zero.

dividendo = float(input("Insira o dividendo: "))
divisor = float(input("Insira o divisor: "))

while divisor == 0:
    divisor = float(input("Valor inválido para o divisor, insira outro: "))

print(f"O resultado da divisão é: \n {dividendo} \n----------- = {dividendo/divisor} \n {divisor}")

