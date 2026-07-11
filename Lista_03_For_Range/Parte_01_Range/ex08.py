# Escreva um programa que leia 5 números do usuário e, ao final, exiba a soma e a média aritmética
# desses números. Use o padrão acumulador com for

soma = 0 

for i in range(5):
    valor = int(input("Insira um valor: "))
    soma += valor 

print(f"A soma dos valores é {soma}")
print(f"A média aritmética dos valores é {soma/5}")
