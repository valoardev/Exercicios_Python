# Escreva um programa que percorra uma lista de nomes utilizando enumerate() e exiba cada nome com
# seu número de ordem, começando em 1.
# Exemplo de saída:
# 1. Ana
# 2. Bruno
# 3. Carla

lista_nomes = ["Gabriel", "Ana", "Pedro","Matheus"]

for numero, nome in enumerate(lista_nomes, start=1):
    print(f"{numero}. {nome}")
    