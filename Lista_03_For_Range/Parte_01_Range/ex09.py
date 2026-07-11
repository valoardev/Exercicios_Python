#Crie um programa que exiba a seguinte sequência usando for e range():
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

linha = ""
for i in range(1,6):
    linha += str(i) + " "
    print(linha)