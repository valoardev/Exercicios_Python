# Estação do ano pelo mês. Leia o número do mês (1–12) e exiba a estação do ano aproximada
# no hemisfério sul: Verão (dez–fev), Outono (mar–mai), Inverno (jun–ago), Primavera (set–nov).

numMes = int(input("Digite o número do mês:"))

if numMes == 12 or numMes == 1 or numMes == 2:
    print("A estação do ano é: Verão")
elif numMes == 3 or numMes == 4 or numMes == 5:
    print("A estação do ano é: Outono")
elif numMes == 6 or numMes == 7 or numMes == 8:
    print("A estação do ano é: Inverno")
elif numMes == 9 or numMes == 10 or numMes == 11:
    print("A estação do ano é: Primavera")
else:
    print("Número do mês inválido. Por favor, insira um número entre 1 e 12.")