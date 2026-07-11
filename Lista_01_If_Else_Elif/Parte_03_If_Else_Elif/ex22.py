#Classificação de IMC. Leia peso (kg) e altura (m), calcule o IMC e 
# classifique: Abaixo do peso (< 18,5), Normal (18,5–24,9), Sobrepeso (25–29,9) ou Obesidade (≥ 30)

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
