# Escreva um programa que leia números do usuário em um laço for de 5 iterações. Se o número for
# negativo, exiba "Valor negativo ignorado" e use continue. Se o número for 0, exiba "Zero encerra a
# entrada" e use break. Caso contrário, acumule a soma dos valores.

soma = 0

for i in range(5):
    numero = float(input("Insira um número: "))
    if numero < 0:
        print("Valor negativo ignorado")
        continue
    elif numero == 0:
        print("Zero encerra a entrada")
        break
    else:
        soma += numero
if soma > 0:
    print(f"A soma dos número foi {soma}")