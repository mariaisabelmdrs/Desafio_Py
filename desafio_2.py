menu = '''
Escolha uma opção:
 [d] - depositar
 [s] - sacar
 [e] - extrato
 [u] - cadastrar usuário
 [c] - cadastrar conta
 [q] - sair

 => '''

saldo = 0.00
limite = 500.00
saque = 0.00
extrato = []  # Inicializado corretamente como lista
numero_saques = 1
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500.0
usuarios = []  # Lista de usuários
proximo_numero_conta = 1  # Sequencial de número de conta

while True:
    opcao = input(menu)

    if opcao == "d":
        def depositar(saldo, extrato):
            print("Depósito")
            valor_depositado = float(input("Qual valor deseja depositar? >> "))
            saldo += valor_depositado  # Atualizando o saldo
            extrato.append(f"Depósito: +R${valor_depositado:.2f}")  # Adiciona o depósito ao extrato
            print(f"Valor depositado: R${valor_depositado}")
            print(f"Saldo atual: R${saldo:.2f}")
            return saldo, extrato  # Retorna o novo saldo e o extrato atualizado
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
        def sacar(saldo, numero_saques, extrato, LIMITE_SAQUES=3, LIMITE_VALOR_SAQUE=500.0):
            print(f"Seu limite de saque atual é de {LIMITE_SAQUES}")
            if numero_saques >= LIMITE_SAQUES:
                print("Você atingiu o limite de saques para hoje.")
                return saldo, numero_saques, extrato  # Retorna o saldo, o número de saques e o extrato não alterados
            
            saque = float(input("Qual valor deseja sacar? >> "))
            
            if saque > LIMITE_VALOR_SAQUE:
                print("Seu limite de valor por saque foi atingido, tente outro valor!")
            elif saque > saldo or saldo == 0:
                print("Não foi possível sacar por falta de saldo!")
            else:
                saldo -= saque  # Atualizando o saldo após saque
                numero_saques += 1  # Incrementa o número de saques após saque bem-sucedido
                extrato.append(f"Saque: -R${saque:.2f}")  # Adiciona o saque ao extrato
                print("Retire as cédulas na saída da máquina.")
                print(f"Saldo atual: R${saldo:.2f}")

            return saldo, numero_saques, extrato  # Retorna o saldo atualizado, o número de saques e o extrato
        saldo, numero_saques, extrato = sacar(saldo, numero_saques, extrato)

    elif opcao == "e":
        def mostrar_extrato(extrato, saldo):
            print("\nExtrato:")
            if not extrato:
                print("Não houve movimentações.")
            else:
                for item in extrato:
                    print(item)
            print(f"Saldo atual: R${saldo:.2f}\n")
        mostrar_extrato(extrato, saldo)

    elif opcao == "u":
        def cadastrar_usuario(usuarios):
            nome = input("Digite o nome do usuário: ")
            nascimento = input("Digite a data de nascimento do usuário: ")
            cpf = input("Digite o CPF do usuário: ")
            endereco = input("Digite o endereço do usuário: ")

            for user in usuarios:  # Verifica se o CPF já está cadastrado
                if user['cpf'] == cpf:
                    print(f"CPF {cpf} já cadastrado. Não é possível cadastrar o usuário.")
                    return False

            novo_usuario = {  # Cria um novo usuário e o adiciona à lista de usuários
                'nome': nome,
                'nascimento': nascimento,
                'cpf': cpf,
                'endereco': endereco,
                'contas': []  # Inicializando a lista de contas do usuário
            }
            usuarios.append(novo_usuario)
            print(f"Usuário {nome} cadastrado com sucesso!")
            return True
        cadastrar_usuario(usuarios)

    elif opcao == "c":
        def cadastrar_conta_corrente(usuarios, proximo_numero_conta):
            cpf = input("Digite o CPF do usuário para cadastrar a conta: ")
            # Procura pelo usuário com o CPF fornecido
            for user in usuarios:
                if user['cpf'] == cpf:
                    agencia = '0001'  # Número fixo da agência
                    numero_conta = f'{proximo_numero_conta:04d}'  # Número da conta sequencial formatado
                    
                    # Cria um dicionário para representar a nova conta corrente
                    nova_conta = {
                        'agencia': agencia,
                        'numero_conta': numero_conta,
                        'nome_titular': user['nome']  # Inclui o nome do titular da conta
                    }
                    # Adiciona a nova conta à lista de contas do usuário
                    user['contas'].append(nova_conta)
                    print(f"Conta corrente {numero_conta} cadastrada para o usuário {user['nome']} com sucesso!")
                    return proximo_numero_conta + 1

            print(f"Usuário com CPF {cpf} não encontrado. Não foi possível cadastrar a conta.")  # Se o CPF não foi encontrado
            return proximo_numero_conta
        proximo_numero_conta = cadastrar_conta_corrente(usuarios, proximo_numero_conta)

    elif opcao == "q":
        print("Obrigada por fazer parte de nossos associados!")
        break

    else: 
        print("Tente novamente, opção inválida!")
