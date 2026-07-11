# Escreva um programa que leia o capital inicial, a taxa de juros mensal (%) e o valor desejado. O
# programa deve calcular e informar quantos meses são necessários para que o capital atinja ou supere o
# valor desejado.

capital_inicial = float(input("Digite seu capital inicial: "))
capital_final = capital_inicial
taxa_juros_mensal = float(input("Digite a taxa de juros mensal em (%): "))
valor_desejado = float(input("Digite o valor que deseja ter ao final: "))
meses = 0
while capital_final < valor_desejado:
    capital_final += capital_final * (taxa_juros_mensal/100)
    meses += 1
print(f"Para o capital inicial de R${capital_inicial:.2f}, com taxa de {taxa_juros_mensal:.1f}% mensais e o valor desejado: R${valor_desejado:.2f}")
print(f"Serão necessários {meses} meses para alcançar a meta desejada!")
print(f"E o valor acumulado seria de R${capital_final:.2f}")
