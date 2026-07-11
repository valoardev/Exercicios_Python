# Escreva um programa que receba uma lista de palavras e exiba cada palavra junto com seu
# comprimento, usando enumerate(). Formato:
# 1. Python (6 letras)
# 2. Programação (11 letras)

palavras = ["Python", "Programação", "Computador", "Dados"]

for indice, palavra in enumerate(palavras, start=1):
    print(f"{indice}. {palavra} ({len(palavra)} letras)")