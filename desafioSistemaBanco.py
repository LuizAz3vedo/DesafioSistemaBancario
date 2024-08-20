class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = 0
        self.limite_saque = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_diarios >= self.limite_saque:
            print("Limite de saques diários atingido.")
        elif valor > 500:
            print("Limite máximo por saque é de R$ 500,00.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.saques_diarios += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def exibir_extrato(self):
        print("\nExtrato:")
        if not self.extrato:
            print("Nenhuma transação realizada.")
        else:
            for transacao in self.extrato:
                print(transacao)
            print(f"\nSaldo atual: R$ {self.saldo:.2f}")

def main():
    banco = Banco()

    while True:
        print("\nEscolha uma operação:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Exibir Extrato")
        print("4 - Sair")
        
        opcao = input("Digite o número da operação desejada: ")

        if opcao == "1":
            valor = float(input("Digite o valor para depósito: "))
            banco.depositar(valor)

        elif opcao == "2":
            valor = float(input("Digite o valor para saque: "))
            banco.sacar(valor)

        elif opcao == "3":
            banco.exibir_extrato()

        elif opcao == "4":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
