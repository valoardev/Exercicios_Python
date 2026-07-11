# Escreva uma função chamada aplicar_desconto que receba o preço original (float) e o percentual de
# desconto (float, com valor padrão de 10.0). A função deve retornar o preço final. No programa
# principal, leia o preço, chame a função uma vez sem informar o desconto (usará 10%) e outra vez
# informando 25%, exibindo ambos os resultados

def aplicar_desconto (preco, desconto=10.0):
    """"
    Função que retorna o preço do produto com desconto
    """
    preco_final = preco - preco*(desconto/100)
    return preco_final

preco = float(input("Qual o preço do produto? "))
resultado = aplicar_desconto(preco)
print(f"O preço final com o desconto de 10% ficou R${resultado:.2f}")
resultado = aplicar_desconto(preco, 25.0)
print(f"O preço final com o desconto de 25% ficou R${resultado:.2f}")




    