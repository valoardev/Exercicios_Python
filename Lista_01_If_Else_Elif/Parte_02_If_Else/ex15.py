# Maior entre dois. Leia dois números e exiba qual é o maior. Se forem iguais, informe que são iguais.

num1 = float(input())
num2 = float(input())

if num1>num2:
    print(num1)
else:
    if num2>num1:
        print(num2)
    else: 
        print("Iguais")