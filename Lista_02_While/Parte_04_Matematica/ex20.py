# Escreva um programa que leia um número inteiro positivo e exiba-o com os dígitos na ordem inversa.
# Exemplo: 1234 → 4321

numero = int(input("Insira um número inteiro positivo: "))

numero_original = numero
invertido = 0

if numero >= 0:
    while numero != 0:
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero = numero // 10

    print(f"O número {numero_original} invertido fica: {invertido}")

else:
    print("Digite um número inteiro positivo.")