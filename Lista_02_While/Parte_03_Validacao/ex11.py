# Escreva um programa que solicite ao usuário um número entre 1 e 100, repetindo a solicitação
# enquanto o valor informado estiver fora desse intervalo. Ao receber um valor válido, exiba-o

numero = int(input("Insira um número: "))

while numero < 1 or numero > 100:
    numero = int(input("Número Inválido, insira outro número: "))
    
print(f"O número inserido é: {numero}")