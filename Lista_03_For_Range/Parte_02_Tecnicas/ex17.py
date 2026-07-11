# Crie um programa que utilize for para verificar se um número inteiro positivo fornecido pelo usuário é
# primo. Utilize a estrutura for-else para exibir a mensagem adequada.

numero = int(input("Digite um número inteiro positivo: "))

if numero <= 1:
    print("Não é primo.")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print("Não é primo.")
            break
    else:
        print("É primo.")