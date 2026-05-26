# Triângulo válido. Leia três valores representando lados de um triângulo. 
# Informe se eles podem ou não formar um triângulo (cada lado deve ser menor que a soma dos outros dois)

A = int(input())
B = int(input())
C = int(input())

if (A<B+C) and (B<A+C) and (C<B+A):
    print("Triângulo válido")
else:
    print("Triângulo invalido")
