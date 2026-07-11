# Crie o esqueleto de um programa de menu com 4 opções 
# (1 – Cadastrar, 2 – Consultar, 3 – Relatório, 4 – Sair). 
# Utilize pass como placeholder nas opções 1, 2 e 3 (ainda não implementadas), e break na
# opção 4 para encerrar o laço
# Dica: use while True com break para sair quando o usuário escolher a opção 4.

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Relatório")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        pass  # ainda não implementado

    elif opcao == 2:
        pass  # ainda não implementado

    elif opcao == 3:
        pass  # ainda não implementado

    elif opcao == 4:
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")