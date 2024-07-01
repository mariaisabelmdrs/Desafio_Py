menu = '''
Escolha uma opção:
 [d] - depositar
 [s] - sacar
 [e] - extrato
 [q] - sair

 => '''

saldo = 0.00
limite = 500.00
saque = 0.00
extrato = ' '
numero_saques = 1
LIMITE_SAQUES = 3

    ##  minhas variáveis
##valor_deposito = 00


while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        print("Qual valor deseja depositar? ")
        valor_depositado = float(input(">> "))
        saldo += valor_depositado  # Atualizando o saldo
        print(f"Valor depositado: R${valor_depositado}")
        print(f"Saldo atual: R${saldo}")

    elif opcao == "s":
        print(f"Seu limite de saque atual é de {LIMITE_SAQUES}")
    
        if LIMITE_SAQUES >= numero_saques:
            print("Só é possível sacar até R$ 500.00")
            print("Qual valor deseja sacar? ")
            saque = float(input(">> "))

            if saque > 500.00:
                print("Seu limite de valor por saque foi atingido, tente outro valor!")

            elif saque > saldo or saldo == 0:
                print("Não foi possível sacar por falta de saldo!")
            else:
                saldo -= saque  # Atualizando o saldo após saque
                print("Retire as cédulas na saída da máquina..")
                LIMITE_SAQUES -= 1  # Decrementa apenas se o saque for bem-sucedido

        else:
            print("Você atingiu o limite de saques para hoje..")


    elif opcao == "e": #extrato
        print(f"Seu saldo atual é de: R${saldo}")
        print(f"Seu último saque foi no valor de: R${saque}")
        print(f"Você ainda pode fazer {LIMITE_SAQUES} saques hoje.")


    elif opcao == "q": #sair
        print("Obrigada por fazer parte de nossos associados!")
        break

    else: 
        print("Tente novamente, opção inválida!")
