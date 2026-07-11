# Escreva uma função chamada celsius_para_fahrenheit que receba uma temperatura em graus Celsius
# (float) e exiba na tela o valor convertido para Fahrenheit, usando a fórmula F = C × 9/5 + 32. No
# programa principal, leia a temperatura e chame a função

def celsius_para_fahrenheit (temperatura):
    """
    Função que converte Celsius para Temperatura e exibe no console
    """
    conversao = temperatura * 9/5 + 32
    print(f"A temperatura {temperatura}°C em Fahrenheit é: {conversao}")

temperatura = float(input("Insira uma temperatura em Celsius: "))
celsius_para_fahrenheit(temperatura)

