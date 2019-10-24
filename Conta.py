class Conta:

    def __init__(self, numero, titular, saldo):
        #variaveis globais
        self.numero = numero
        self.titular = titular
        self.saldo = saldo


    def sacar(self, valor):
        self.saldo = self.saldo - valor
        return self.saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo

    def getSaldo(self):
        return self.saldo

    def getNumero(self):
        return self.numero

    def getTitular(self):
        return self.titular

    def setTitular(self, novoTitular):
        self.titular = novoTitular

    def setNumero(self, novoNumero):
        self.numero = novoNumero

    def setSaldo(self, novoSaldo):
        self.saldo = novoSaldo

def main():
    #Criando conta
    conta = Conta(14052, "Camila", 150)
    conta1 = Conta(26082, "Vitor", 200)
    conta2 = Conta(35842, "Priscila", 320)

    #Verificando valores na conta
    print("Conta Camila: ", conta.saldo)
    print("Conta Vitor: ", conta1.saldo)
    print("Conta Priscila: ", conta2.saldo)

    #mudando titular
    print("Conta Camila: ", conta.getTitular())
    conta.setTitular("Camila Ascendina")
    print("Conta Camila: ", conta.getTitular())

if __name__ == '__main__':
    main()