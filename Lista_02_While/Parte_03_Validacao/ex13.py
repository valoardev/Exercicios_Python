# Escreva um programa que leia a idade de uma pessoa, aceitando apenas valores entre 0 e 130.
# Enquanto o valor for inválido, o programa deve exibir uma mensagem de erro e solicitar nova entrada.

idade = -1

while idade < 0 or idade > 130:
    idade = int(input("Digite uma idade válida: "))
    if idade > 130 or idade < 0:
        print("Idade inválida, digite outra")

print(f"Sua idade é {idade}")