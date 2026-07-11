# Classificação de triângulo por lados. Leia três valores. 
# Primeiro verifique se formam um triângulo válido. 
# Se formarem, classifique-o como Equilátero (3 lados iguais), Isósceles (2 lados iguais) ou Escaleno (todos diferentes).

A = int(input("Digite o valor do lado A do triângulo: "))
B = int(input("Digite o valor do lado B do triângulo: "))
C = int(input("Digite o valor do lado C do triângulo: "))

if (A<B+C) and (B<A+C) and (C<B+A):
    if A == B == C:
        print("É um Triângulo válido e equilátero")
    elif A == B or B == C or A == C:
        print("É um Triângulo válido e isósceles")
    else:
        print("É um Triângulo válido e escaleno")
else:
    print("Não é um Triângulo válido")