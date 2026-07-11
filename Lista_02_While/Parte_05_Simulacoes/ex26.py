# Escreva um programa que leia um valor inteiro de saque e determine o menor número de cédulas
# necessárias para compor esse valor, usando cédulas de 200, 100, 50, 20, 10, 5 e 2 reais. Utilize while
# para processar cada tipo de cédula. 

valor = int(input("Digite o valor do saque: "))
cedulas_200 = 0
cedulas_100 = 0
cedulas_50 = 0
cedulas_20 = 0
cedulas_10 = 0
cedulas_5 = 0
cedulas_2 = 0

while valor >= 200:
    valor -= 200
    cedulas_200 += 1
while valor >= 100:
    valor -= 100
    cedulas_100 += 1
while valor >= 50:
    valor -= 50
    cedulas_50 += 1
while valor >= 20:
    valor -= 20
    cedulas_20 += 1
while valor >= 10:
    valor -= 10
    cedulas_10 += 1
while valor >= 5:
    valor -= 5
    cedulas_5 += 1
while valor >= 2:
    valor -= 2
    cedulas_2 += 1

print("\nCédulas utilizadas:")
if valor <= 0:
    print("Não é possível sacar este valor!")
if cedulas_200 > 0:
    print(f"{cedulas_200} cédula(s) de R$200")
if cedulas_100 > 0:
    print(f"{cedulas_100} cédula(s) de R$100")
if cedulas_50 > 0:
    print(f"{cedulas_50} cédula(s) de R$50")
if cedulas_20 > 0:
    print(f"{cedulas_20} cédula(s) de R$20")
if cedulas_10 > 0:
    print(f"{cedulas_10} cédula(s) de R$10")
if cedulas_5 > 0:
    print(f"{cedulas_5} cédula(s) de R$5")
if cedulas_2 > 0:
    print(f"{cedulas_2} cédula(s) de R$2")
if valor > 0:
    print(f"Restou R${valor}, que não pode ser sacado com as cédulas disponíveis.")