# Crie um programa que exiba todos os números primos entre 2 e 100. Para cada número do intervalo,
# use um laço for interno com break para testar divisibilidade, e a estrutura for-else para identificar os
# primos.

for i in range(2,101):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i, end=",")