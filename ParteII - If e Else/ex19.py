# Troco ou valor insuficiente. Leia o preço de um produto e o valor pago. 
# Se o pagamento for suficiente, exiba o troco; caso contrário, informe quanto falta

preço = float(150)
valor = float(input())

if valor >= preço:
    print("Troco é: R$",valor-preço)
else: 
    print("Falta: R$",preço-valor)
