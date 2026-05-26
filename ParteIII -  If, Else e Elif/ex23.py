# Faixa etária. Leia a idade e classifique: 
# Criança (0–11), Adolescente (12–17), Adulto (18–59) ou Idoso (60+)

idade = int(input("Insira a sua idade: "))

if idade > 0 and idade <= 11:
    print("Criança")
elif idade >= 12 and idade <=17:
    print("Adolescente")
elif idade >= 18 and idade <=59:
    print("Adulto")
else:
    print("Idoso")
    
