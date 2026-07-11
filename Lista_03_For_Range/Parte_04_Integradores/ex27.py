# Escreva um programa que leia números inteiros do usuário em um laço. Use try-except com continue
# para ignorar entradas inválidas (não numéricas). Quando o usuário digitar -1, encerre com break. Ao
# final, exiba a soma e a quantidade de números válidos digitados.
# Dica: combine while True, try-except ValueError, continue e break.

soma = 0
quantidade = 0
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero == -1:
            print("Programa encerrado")
            break
        else:
            soma += numero
            quantidade += 1
    except ValueError:
        print("Valor incorreto digitado")
        continue
print(f"Foram digitados {quantidade} números válidos")
print(f"A soma dos números válidos é {soma}")

