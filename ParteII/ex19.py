preço = float(150)
valor = float(input())

if valor >= preço:
    print("Troco é: R$",valor-preço)
else: 
    print("Falta: R$",preço-valor)
