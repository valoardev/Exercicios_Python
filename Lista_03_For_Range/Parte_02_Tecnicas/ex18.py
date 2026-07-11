# Escreva um programa que receba uma frase do usuário e conte quantas vogais, consoantes e espaços
# existem na frase, utilizando um laço for.

frase = input("Digite uma frase: ")

vogais = 0
consoantes = 0
espacos = 0

for caractere in frase:
    if caractere.lower() in "aeiou":
        vogais += 1
    elif caractere.lower() >= "a" and caractere.lower() <= "z":
        consoantes += 1
    elif caractere == " ":
        espacos += 1

print("Quantidade de vogais:", vogais)
print("Quantidade de consoantes:", consoantes)
print("Quantidade de espaços:", espacos)