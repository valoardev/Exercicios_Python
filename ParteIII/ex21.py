nota = float(input("Insira a nota:"))

if nota >= 9:
    print("Parabéns! Você tirou A")
elif nota >=7:
    print("Parabéns! Você tirou B")
elif nota >=5:
    print("Passou! Tirou C")
elif nota >=3:
    print("Não passou! Tirou D")
else:
    print("Reprovou, tirou F")
