from datetime import date
from typing import Dict, List


class Titular:
    def __init__(self, nome: str, cpf: str, dt_nasc: date) -> None:
        self._nome: str = nome
        self._cpf: str = cpf
        self._dt_nasc: date = dt_nasc

    @property
    def nome_titular(self) -> str:
        return self._nome
    
    @nome_titular.setter
    def nome_titular(self, nome: str) -> None:
        self._nome = nome

    @property
    def cpf(self) -> str:
        return self._cpf
    
    @property
    def data_nascimento(self) -> str:
        return self._dt_nasc

class ContaCorrente:
    def __init__(self, titular: Titular, agencia: str, conta: str ):
        self._titular: Titular = titular
        self._agencia: str = agencia
        self._conta: str = conta
        self._saldo: float = 0.0
        self._extrato: List[Dict[str, str]] = []
    
    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def conta(self) -> str:
        return self._conta
    
    @property
    def saldo(self) -> float:
        return self._saldo
    
    @property
    def titular(self) -> Titular:
        return self._titular
    
    def _adiciona_extrato(self, tipo: str, valor: float):
        valor_formatado = '{:.2f}'.format(valor)
        if tipo.upper() == 'E':
            self._extrato.append({ 'key': 'E', 'value': valor_formatado})
        else:
            self._extrato.append({ 'key': 'S', 'value': valor_formatado})

    def _msg_resposta(self, sucesso: bool):
        if sucesso:
            print('Operação realizada com sucesso.')
        else:
            print('Falha ao realizar operação.')

    def deposito(self, valor_deposito: float) -> None:
        if valor_deposito > 0.00:
            self._saldo += valor_deposito
            self._adiciona_extrato(tipo='E', valor=valor_deposito)
            self._msg_resposta(True)
        else:
            self._msg_resposta(False)
    
    def pagamento(self, valor_pagamento: float) -> None:
        if self._saldo >= valor_pagamento:
            self._saldo -= valor_pagamento
            self._adiciona_extrato(tipo='S', valor=valor_pagamento)
            self._msg_resposta(True)
        else:
            self._msg_resposta(False)

    def saque(self, valor_saque: float) -> None:
        if self._saldo >= valor_saque:
            self._saldo -= valor_saque
            self._adiciona_extrato(tipo='S', valor=valor_saque)
            self._msg_resposta(True)
        else:
            self._msg_resposta(False)
    
    def transferencia(self, valor_transferencia: float, conta_destino) -> None:
        if self._saldo >= valor_transferencia:
            self._saldo -= valor_transferencia
            self._adiciona_extrato(tipo='S', valor=valor_transferencia)
            conta_destino.deposito(valor_transferencia)
            self._msg_resposta(True)
        else:
            self._msg_resposta(False)
        
    def extrato(self):
        print(f'Agência: {self.agencia}')
        print(f'Conta: {self.conta}')
        print(f'Nome do titular: {self.titular.nome_titular}')
        print(f'CPF do titular: {self.titular.cpf}')
        print('Saldo: R$', '{:.2f}'.format(self.saldo), sep=' ')
        for mov in self._extrato:
            print(f'\t{mov["key"]}: R$ {mov["value"]}')
