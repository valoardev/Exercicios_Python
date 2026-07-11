# Escreva um programa que gere e exiba o Triângulo de Pascal com n linhas (informado pelo usuário).
# Utilize laços for aninhados. Cada linha deve ser exibida formatada e centralizada. Utilize pass como
# placeholder se decidir separar a lógica de cálculo da lógica de exibição em etapas distintas.
# Exemplo para n=5:
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

while True:
    try:
        n = int(input("Insira o número de linhas para o triângulo de pascoal: "))
        break
    except ValueError:
        print("Insira um valor válido!")
        continue

for i in range(n):
    valor = 1
    linha = []

    for j in range(i + 1):
        linha.append(valor)
        valor = valor * (i - j) // (j + 1)

    print(" " * (n - i), end="")
    for num in linha:
        print(num, end=" ")
    print()
    