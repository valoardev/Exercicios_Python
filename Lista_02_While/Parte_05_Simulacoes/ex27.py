# Escreva um programa que defina um número secreto (fixo, por exemplo, 42) e peça ao usuário para
# adivinhar. A cada tentativa, o programa deve informar se o palpite foi alto ou baixo. O laço termina
# quando o usuário acerta, e o programa deve informar o total de tentativas. 

numero_secreto = 42
numero = int(input("Tente adivinhar o valor do número secreto: "))
i = 1
while numero !=  numero_secreto:
    if numero > numero_secreto:
        print("Seu palpite foi mais alto! Chute um número mais baixo")
    else: 
        print("Seu palpite foi mais baixo! Chute um número mais alto")
    i += 1
    numero = int(input("Chute outro número: "))
print(f"Parabéns, você acertou! o número secreto é {numero_secreto}, Você acertou em {i} tentativa(s)")