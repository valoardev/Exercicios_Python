print("CARDÁPIO:\nLanche...R$8,00\nSuco...R$5,00\nCafé...R$2,50\nÁgua...R$3,00")

opcao = input("Insira a opção que deseja: ").lower()

if opcao == "lanche":
    print("Lanche...R$8,00")
elif opcao == "suco":
    print("Suco...R$5,00")
elif opcao == "café":
    print("Café...R$2,50")
elif opcao == "água":
    print("Água...R$3,00")
else:
    print("Selecione uma opção válida do cardápio")

      