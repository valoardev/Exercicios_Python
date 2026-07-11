# Faça um programa que leia n números fornecidos pelo usuário e determine o maior e o menor valor
# digitado. Use o padrão de acumulação com for, inicializando maior e menor como None.

n = int(input("Quantos números serão digitados? "))

maior = None
menor = None

for i in range(n):
    numero = float(input(f"Digite o {i+1}º número: "))

    if maior is None:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

print(f"Maior valor digitado: {maior:.0f}")
print(f"Menor valor digitado: {menor:.0f}")
