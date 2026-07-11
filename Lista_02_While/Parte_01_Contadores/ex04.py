# Escreva um programa que exiba todas as potências de 2 que sejam menores ou 
# iguais a um valor limite informado pelo usuário

limite = int(input("Insira o valor limite: "))
n = 1

print(f"Potências de 2 menores que {limite}:")
while n*2 <= limite:
    print(f"{n}x2 = {n*2}")
    n+=1
