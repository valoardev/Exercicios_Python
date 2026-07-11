# A cidade A possui 80.000 habitantes e cresce 3% ao ano. A cidade B possui 200.000 habitantes e
# cresce 1,5% ao ano. Escreva um programa que calcule em quantos anos a população de A ultrapassará
# a de B. Caso A nunca ultrapasse B em até 500 anos, informe essa condição.

cidadeA = 80000
cidadeB = 200000
anos = 0

while cidadeA < cidadeB and anos < 500:
    cidadeA += cidadeA * (3/100)
    cidadeB += cidadeB * (1.5/100)
    anos += 1

if cidadeA > cidadeB: 
    print(f"A cidade A possui atualmente {cidadeA:.0f} habitantes e a cidade B possui atualmente {cidadeB:.0f} habitantes")
    print(f"A cidade A passou a população da cidade B em {anos} anos")
else:
    print(f"Mesmo após 500 anos, a cidade A não ultrapassou a população da cidade B")
