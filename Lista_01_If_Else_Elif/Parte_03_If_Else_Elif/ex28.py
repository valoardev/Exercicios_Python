# Semáforo. Leia a cor do semáforo (verde, amarelo ou vermelho) e exiba a ação correspondente:
# Siga em frente, Atenção ou Pare.

corSemaforo = input("Digite a cor do semáforo (vermelho, amarelo ou verde): ").lower()

if corSemaforo == "vermelho":
    print("Pare!")
elif corSemaforo == "amarelo":
    print("Atenção!")
elif corSemaforo == "verde":
    print("Siga em frente!")
else:
    print("Cor do semáforo inválida. insira (Vermelho, Amarelo ou Verde).")