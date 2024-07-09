class Transacao:
    def __init__(self, valor):
        self.valor = valor

    def realizar(self, conta):
        raise NotImplementedError("Subclasses devem implementar este método")


class Deposito(Transacao):
    def realizar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(f"Depósito: +R${self.valor:.2f}")


class Saque(Transacao):
    def realizar(self, conta):
        if self.valor > conta.saldo:
            print("Saldo insuficiente!")
            return False
        elif conta.numero_saques >= conta.LIMITE_SAQUES:
            print("Limite de saques diários atingido!")
            return False
        elif self.valor > conta.LIMITE_VALOR_SAQUE:
            print("Limite de valor por saque atingido!")
            return False
        else:
            conta.saldo -= self.valor
            conta.numero_saques += 1
            conta.historico.adicionar_transacao(f"Saque: -R${self.valor:.2f}")
            return True


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def mostrar_extrato(self, saldo):
        print("\nExtrato:")
        if not self.transacoes:
            print("Não houve movimentações.")
        else:
            for item in self.transacoes:
                print(item)
        print(f"Saldo atual: R${saldo:.2f}\n")


class Conta:
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500.0

    def __init__(self, agencia, numero, cliente):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0
        self.numero_saques = 0
        self.historico = Historico()

    def __str__(self):
        return f"Conta {self.numero} - Agência {self.agencia} - Cliente {self.cliente.nome}"


class Cliente:
    def __init__(self, nome, nascimento, cpf, endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


clientes = []
proximo_numero_conta = 1

menu = '''
Escolha uma opção:
 [d] - depositar
 [s] - sacar
 [e] - extrato
 [u] - cadastrar usuário
 [c] - cadastrar conta
 [q] - sair

 => '''

while True:
    opcao = input(menu)

    if opcao == "d":
        cpf = input("Digite o CPF do titular da conta: ")
        cliente = next((c for c in clientes if c.cpf == cpf), None)
        if cliente:
            conta = cliente.contas[0]  # Supondo uma única conta por cliente para simplificar
            valor = float(input("Qual valor deseja depositar? >> "))
            deposito = Deposito(valor)
            deposito.realizar(conta)
        else:
            print("Cliente não encontrado!")

    elif opcao == "s":
        cpf = input("Digite o CPF do titular da conta: ")
        cliente = next((c for c in clientes if c.cpf == cpf), None)
        if cliente:
            conta = cliente.contas[0]
            valor = float(input("Qual valor deseja sacar? >> "))
            saque = Saque(valor)
            saque.realizar(conta)
        else:
            print("Cliente não encontrado!")

    elif opcao == "e":
        cpf = input("Digite o CPF do titular da conta: ")
        cliente = next((c for c in clientes if c.cpf == cpf), None)
        if cliente:
            conta = cliente.contas[0]
            conta.historico.mostrar_extrato(conta.saldo)
        else:
            print("Cliente não encontrado!")

    elif opcao == "u":
        nome = input("Digite o nome do usuário: ")
        nascimento = input("Digite a data de nascimento do usuário: ")
        cpf = input("Digite o CPF do usuário: ")
        endereco = input("Digite o endereço do usuário: ")

        if any(c.cpf == cpf for c in clientes):
            print(f"CPF {cpf} já cadastrado. Não é possível cadastrar o usuário.")
        else:
            novo_cliente = Cliente(nome, nascimento, cpf, endereco)
            clientes.append(novo_cliente)
            print(f"Usuário {nome} cadastrado com sucesso!")

    elif opcao == "c":
        cpf = input("Digite o CPF do usuário para cadastrar a conta: ")
        cliente = next((c for c in clientes if c.cpf == cpf), None)
        if cliente:
            agencia = '0001'
            numero_conta = f'{proximo_numero_conta:04d}'
            nova_conta = Conta(agencia, numero_conta, cliente)
            cliente.adicionar_conta(nova_conta)
            proximo_numero_conta += 1
            print(f"Conta corrente {numero_conta} cadastrada para o usuário {cliente.nome} com sucesso!")
        else:
            print(f"Usuário com CPF {cpf} não encontrado. Não foi possível cadastrar a conta.")

    elif opcao == "q":
        print("Obrigada por fazer parte de nossos associados!")
        break

    else: 
        print("Tente novamente, opção inválida!")
