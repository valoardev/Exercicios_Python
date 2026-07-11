# Escreva um programa que exiba o menu abaixo e solicite a escolha do usuário. Enquanto a opção for
# inválida, o menu deve ser reexibido. Quando válida, exiba a opção escolhida.
# [1] Cadastrar
# [2] Consultar
# [3] Sair

opcao = 4
while opcao != 1 and opcao != 2 and opcao !=3:
    print("[1] Cadastrar \n[2] Consultar \n[3] Sair")
    opcao = int(input("Selecione uma das opções acima: "))
    if opcao != 1 and opcao != 2 and opcao !=3:
        print("Digite uma opção válida")
if opcao == 1:
    print(f"Opção escpçhida é Cadastrar")
elif opcao == 2:
    print(f"Opção escolhida é Consultar")
else:
    print(f"Opção escolhida é Sair")

