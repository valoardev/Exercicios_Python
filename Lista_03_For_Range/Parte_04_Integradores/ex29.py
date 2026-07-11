# Escreva um programa que simule um sistema de cadastro simplificado. O programa deve:
# a) Usar while True para manter o menu ativo;
# b) Oferecer opções: 1 – Adicionar nome, 2 – Listar nomes, 3 – Buscar nome, 4 – Sair;
# c) Na opção 1, adicionar o nome a uma lista;
# d) Na opção 2, usar for com enumerate() para listar os nomes;
# e) Na opção 3, usar for-else com break para buscar;
# f) Na opção 4, usar break para encerrar;
# g) Para opções inválidas, usar continue.


lista_nomes = []
while True:
    print("\n==== OPÇÕES ====")
    print("1 - Adicionar nome\n2 - Listar nomes\n3 - Buscar nome\n4 - Sair")
    try:
        opcao = int(input("Escolha a opção: "))
    except ValueError:
        print("Opção inválida")
        continue
    if opcao == 1:
        adiciona = input("Qual nome deve ser adicionado: ")
        lista_nomes.append(adiciona)
    elif opcao == 2:
        print("\n=== LISTA DE NOMES ===")
        for indice, nome in enumerate(lista_nomes,start=1):
            print(f"{indice} - {nome}")
    elif opcao == 3:
        busca = input("Qual nome deseja buscar na lista: ")
        for indice, nome in enumerate(lista_nomes,start=1):
            if nome == busca:
                print(f"Nome encontrado na posição °{indice}")
                break
        else:
            print("Nome não encontrado!")
    elif opcao == 4:
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida")
        continue
