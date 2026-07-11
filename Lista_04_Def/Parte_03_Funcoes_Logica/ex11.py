# Escreva uma função chamada eh_triangulo que receba três lados (float) e retorne True se eles formam
# um triângulo válido (cada lado deve ser menor que a soma dos outros dois) ou False caso contrário.
# Em seguida, escreva uma segunda função chamada tipo_triangulo que receba os mesmos três lados e
# retorne “Equilátero”, “Isósceles” ou “Escaleno”. No programa principal, leia os três lados, use
# eh_triangulo para verificar a validade e, se válido, chame tipo_triangulo e exiba a classificação

def eh_triangulo (lado1, lado2, lado3):
    if lado1 >= (lado2 + lado3) or lado2 >= (lado1 + lado3) or lado3 >= (lado1 + lado2):
        return False
    else:
        return True
def tipo_triangulo (lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3:
        return "Equilátero"
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        return "Escaleno"
    else:
        return "Isósceles"

lado1 = float(input("Insira o valor do Lado 1: "))
lado2 = float(input("Insira o valor do Lado 2: "))
lado3 = float(input("Insira o valor do Lado 3: "))
valido = eh_triangulo(lado1,lado2,lado3)
if valido:
    tipo = tipo_triangulo(lado1,lado2,lado3)
    print(f"O seu triângulo é válido e é um triângulo {tipo} ")
else: 
    print("O seu triângulo não é válido e não possui um tipo")