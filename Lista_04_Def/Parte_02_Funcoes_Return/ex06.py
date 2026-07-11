# Escreva uma função chamada area_retangulo que receba a base (float) e a altura (float) como
# parâmetros e retorne a área. No programa principal, leia os valores, chame a função, armazene o
# resultado em uma variável e exiba-o com duas casas decimais

def area_retangulo (base, altura):
    """
    Função que faz o cálculo da área de um retângulo
    """
    area = base*altura
    return area
    

base = float(input("Insira a base do retângulo: "))
altura = float(input("Insira a altura do retângulo: "))
resultado = area_retangulo(base, altura)
print(f"A área deste retângulo é {resultado:.2f}")
