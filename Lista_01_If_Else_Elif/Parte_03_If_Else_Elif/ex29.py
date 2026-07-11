# Pedra, papel e tesoura. Leia a jogada do jogador 1 e do jogador 2 (pedra, papel ou tesoura).
# Exiba quem venceu ou se houve empate

jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").lower()
jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura: ").lower()

if jogador1 == jogador2:
    print("Empate!")
elif (jogador1 == "pedra" and jogador2 == "tesoura") \
    or (jogador1 == "papel" and jogador2 == "pedra") \
    or (jogador1 == "tesoura" and jogador2 == "papel"):
    print("Jogador 1 venceu!")
elif (jogador2 == "pedra" and jogador1 == "tesoura") \
    or (jogador2 == "papel" and jogador1 == "pedra") \
    or (jogador2 == "tesoura" and jogador1 == "papel"):
    print("Jogador 2 venceu!")
else:
    print("Entrada inválida. Por favor, escolha pedra, papel ou tesoura.")

