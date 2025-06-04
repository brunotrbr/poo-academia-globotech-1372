# # Herança e Polimorfismo

# ## Herança

# - Estender a funcionalidade de uma classe. 


# - Conta (pai), com atributos e métodos comuns a todas as contas bancárias.
# - ContaCorrente, ContaPoupança (contas filhas), sendo que a conta corrente pode realizar pagamentos e transferências, enquanto a conta poupança não.
# - Titular não será modificada

# Exemplo da classe Conta e início da classe ContaCorrente:
# OBS: Foi feita uma mudança da classe "ContaCorrente" vista na aula 5 para a classe "Conta" abaixo. Você consegue identificar o que foi alterado? Por qual motivo?

from aula_5.conta_corrente import Titular
from typing import List, Dict
from datetime import date

class Conta:
  def __init__(self, titular: Titular, agencia: str, conta: str):
        self._titular: Titular = titular
        self._agencia: str = agencia
        self._conta: str = conta
        self._saldo: float = 0.0
        self._extrato: List[Dict[str, str]] = []

  @property
  def titular(self) -> Titular:
      return self._titular

  @property
  def agencia(self) -> str:
      return self._agencia

  @property
  def conta(self) -> str:
      return self._conta

  @property
  def saldo(self) -> float:
      return self._saldo
  
  def _adicionar_extrato(self, tipo: str, valor: float):
      valor_formatado = '{:.2f}'.format(valor)
      self._extrato.append({'key': tipo.upper(), 'value': valor_formatado})

  def _msg_resposta(self, sucesso: bool, nome_operacao: str) -> None:
      if sucesso:
          print(f'Operação realizada com sucesso. Operação: {nome_operacao}')
      else:
          print(f'Falha ao realizar operação. Operação: {nome_operacao}')

  def _saidas(self, valor: float, nome_operacao: str) -> bool:
        if self._saldo >= valor:
            self._saldo -= valor
            self._adicionar_extrato(tipo='s', valor=valor)
            self._msg_resposta(sucesso=True, nome_operacao=nome_operacao)
        else:
            self._msg_resposta(sucesso=False, nome_operacao=nome_operacao)
            
  def deposito(self, valor: float) -> None:
      nome_operacao = 'Deposito'
      if valor > 0.0:
          self._saldo += valor
          self._adicionar_extrato(tipo='e', valor=valor)
          self._msg_resposta(sucesso=True, nome_operacao=nome_operacao)
      else:
          self._msg_resposta(sucesso=False, nome_operacao=nome_operacao)

  def saque(self, valor: float) -> None:
      self._saidas(valor=valor, nome_operacao='Saque')

  def extrato(self):
      print(f'Agencia: {self._agencia}')
      print(f'Conta: {self._conta}')
      print(f'Titular: {self.titular._nome}')
      print(f'CPF do titular: {self._titular.cpf}')
      print('Saldo: R$', '{:.2f}'.format(self._saldo), sep=' ')
      for mov in self._extrato:
          print(f'\t{mov["key"]}: R$ {mov["value"]}')

class ContaCorrente(Conta):
    def __init__(self, titular: Titular, agencia: str, conta: str):
        super().__init__(titular, agencia, conta)

    # TODO: Implementar métodos "pagamento" e "transferencia".

# TODO: Implementar a classe ContaPoupanca



# No exemplo acima:

# - "Conta" é a classe "base", "pai" ou "super classe"
# - "ContaCorrente" e "ContaPoupanca" são classes "derivadas" ou classes "filhas" da classe "Conta"
# - "ContaCorrente" herda da classe "Conta" ou "ContaCorrente" estende a classe "Conta"

# - Objetos da classe "ContaCorrente" possuem todas as funcionalidades da classe "Conta" mais algumas funcionalidades extras.

# Em outras palavras, uma "ContaCorrente" é uma "Conta".

# - Sempre que uma função esperar receber como parâmetro um objeto do tipo "Conta", podemos passar um objeto do tipo "ContaCorrente" ou "ContaPoupanca", dado que ambas são "Conta".

## Como ver se um objeto é instancia de outro?

# - Função "isinstance()"
dt_nasc = date(year=1991, month=8, day=6)
t1 = Titular('Pedro', 'Engenheiro de dados', dt_nasc)
cc1 = ContaCorrente(t1, '001', 'c101')
print(isinstance(cc1, ContaCorrente))


# ## Polimorfismo

# Capacidade que uma classe filha tem de ter métodos com o mesmo nome de sua classe pai, e o programa saber qual método deve ser invocado

# Ou seja, capacidade do objeto de assumir diferentes formas (polimorfismo)

# &nbsp;

# Considerando nosso exemplo acima, vamos supor que os bancos congelem os saques da "ContaPoupanca" acima de R$ 100,00, mas permitam realizar o saque da "ContaCorrente". Saques da poupança abaixo de R$ 100,00 ainda são permitidos. De que forma podemos implementar isso?

# TODO Implementar o método "saque" na classe "ContaPoupanca" que não permita realizar saques acima de R$ 100,00.