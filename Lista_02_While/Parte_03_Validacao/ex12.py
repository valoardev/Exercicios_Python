# Escreva um programa que peça ao usuário uma senha numérica.
# O programa deve continuar pedindo enquanto a senha digitada for diferente de 2025. Ao acertar, exiba "Acesso liberado" e 
# quantas tentativas foram necessárias

senha = 0
i = 0
while senha != 2025:
    senha = int(input("Insira uma senha númerica: "))
    i += 1

print(f"Acesso liberado! foram feitas {i} tentativas de acesso")