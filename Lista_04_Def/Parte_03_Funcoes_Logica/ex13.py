# Escreva uma função chamada calcular_imposto que receba o salário bruto (float) e retorne o valor do
# imposto conforme as faixas: até R$ 1.500,00 → isento (0.0); de R$ 1.500,01 a R$ 3.500,00 → 15%;
# acima de R$ 3.500,00 → 27,5%. Em seguida, escreva uma função chamada salario_liquido que receba
# o salário bruto, chame internamente calcular_imposto e retorne o salário líquido (bruto − imposto). No
# programa principal, leia o nome (str) e o salário bruto do funcionário, chame salario_liquido e exiba
# um contracheque formatado com nome, bruto, imposto e líquido.

def calcular_imposto (salario):
    if salario <= 1500:
        return 0
    elif salario <= 3500:
        return salario*0.15
    return salario*0.275
def salario_liquido (salario):
    return salario - calcular_imposto(salario)

nome = input("Insira seu nome completo: ")    
salario = float(input("Insira o seu salário bruto: "))
print(f"=== CONTRA CHEQUE ===\nNome: {nome}\nSalário Bruto: R${salario:.2f}\nImposto: R${calcular_imposto(salario):.2f}\nSalário Líquido: R${salario_liquido(salario):.2f}")