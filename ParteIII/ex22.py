peso =  float(input("Insira seu peso em kg:"))
altura = float(input("Insira sua altura em metros:"))
IMC = peso/altura**2
print(IMC)

if IMC < 18.5:
    print("Abaixo do peso")
elif (IMC >= 18.5) and (IMC <= 24.9):
    print("Normal")
elif (IMC >= 25) and (IMC <= 29.9):
    print("Sobrepeso")
else:
    print("Obesidade")
