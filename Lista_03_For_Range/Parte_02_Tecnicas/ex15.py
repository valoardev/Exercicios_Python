# Faça um programa que calcule a potência de um número sem usar o operador **. O programa deve ler
# a base e o expoente do usuário, e utilizar um laço for para realizar multiplicações sucessivas.
# Exemplo: base=3, expoente=4 → 3 × 3 × 3 × 3 = 81

base = int(input("Digite o número da Base: "))
expoente = int(input("Digite o número do expoente: "))
resultado = 1
for i in range(expoente):  
    resultado *= base
print(f"A resultado desta potência é {resultado}")