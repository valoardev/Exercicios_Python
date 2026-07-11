# Escreva uma função chamada gerar_secreto que não receba parâmetros e retorne um número inteiro
# aleatório entre 1 e 50 (use import random e random.randint). Escreva outra função chamada dar_dica
# que receba o palpite (int) e o número secreto (int) e retorne a string “Maior”, “Menor” ou “Acertou”.
# No programa principal, use gerar_secreto para obter o número, depois crie um laço while que peça
# palpites ao usuário, chame dar_dica, exiba a dica e conte as tentativas. Ao acertar, exiba o total de
# tentativas.
import random
def gerar_secreto():
    return random.randint(1, 50) 
def dar_dica(palpite, numero_secreto):
    if palpite > numero_secreto:
        return "Menor"
    elif palpite < numero_secreto:
        return "Maior"
    return "Acertou"

numero_secreto = gerar_secreto()
tentativas = 0
while True:
    palpite = int(input("Insira o seu palpite entre 1 a 50: "))
    if not 1 <= palpite <= 50:
        print("Digite um número entre 1 e 50.")
        continue
    tentativas += 1
    resultado = dar_dica(palpite,numero_secreto)
    if resultado == "Acertou":
        print(F"Você acertou! o número é {numero_secreto}, você fez {tentativas} tentativa(s)")
        break
    else:
        print(f"Digite um valor {resultado}")

