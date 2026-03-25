class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self._titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self._saldo:
            print("Saldo insuficiente.")
        else:
            self._saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")

    def exibir_saldo(self):
        print(f"Titular: {self._titular}")
        print(f"Saldo atual: R${self._saldo}")

conta = ContaBancaria("João", 100)

conta.depositar(50)
conta.sacar(30)
conta.exibir_saldo()