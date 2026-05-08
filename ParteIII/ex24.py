temperatura = float(input("Insira a temperatura em Celsius: "))

if temperatura <= 0:
    print("Gelado")
elif temperatura >=1 and temperatura <=15:
    print("Frio")
elif temperatura >=16 and temperatura <=25:
    print("Agradável")
elif temperatura >=26 and temperatura <=35:
    print("Quente")
else:
    print("Muito Quente")
    