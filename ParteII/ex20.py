A = int(input())
B = int(input())
C = int(input())

if (A<B+C) and (B<A+C) and (C<B+A):
    print("Triângulo válido")
else:
    print("Triângulo invalido")
