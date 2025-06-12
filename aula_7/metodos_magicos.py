# # Métodos mágicos

# - Métodos **pré-definidos** existentes em todos os objetos, com **invocação automática**

# - Normalmente não são executados pelo usuário, mas podem ser ser caso haja necessidade

# - Podem ser sobrescritos para alterar o comportamento de uma classe

# - Padrão de nome: __dunder__ (double underscore): 

# ```python
# __name__(parametros)
# ```

# Para ver seu funcionamento, vamos usar a classe Drex abaixo:

class Drex:
    def __init__(self, valor):
        self._valor = valor

dir(Drex)

# ## Métodos de construção

# Init, o construtor que já vimos como funciona.

drex = Drex(5)

########################################################################################################

# ## Métodos de representação

# Vamos imprimir a variável drex, e pedir a representação dele como string.

drex = Drex(5)
print(drex)
print(str(drex))

# O que aconteceu?

# Por padrão o print em uma instância de uma classe retorna o endereço de memória em que aquele objeto está alocado.

# O mesmo não ocorre com listas, tuplas, dicionários, etc.

lista = [1, 2]
print(lista)
tupla = (3, 5)
print(tupla)
dicionario = {'chave': 'valor'}
print(dicionario)

# O motivo? O método mágico __str__

# ### __str__

# - Exibe a representação daquele objeto como string
# - O print, internamente, chama o método mágico __str__
# - Vamos reescrever seu funcionamento, para que não apareça mais o endereço de memória
 
class Drex:
  def __init__(self, valor):
    self._valor = valor

  def __str__(self):
    arredondado = round(self._valor, 2)
    return f"R$ {arredondado:.2f}"

drex = Drex(5)
print(drex)
print(str(drex))

drex = Drex(4.976)
print(drex)
print(str(drex))

# Lembrando, o __str__ seria equivalente ao `ToString()` do Java e do C#

# ## Observação

# - Tecnicamente, __str__ está "ensinando" o python a como gerar uma string a partir de seu objeto. Podemos usar também outras coerções de tipos, como `__int__`, `__bool__` e `__float__`.

class Drex:
  def __init__(self, valor):
    self._valor = valor

  def __str__(self):
    arredondado = round(self._valor, 2)
    return f'R$ {arredondado:.2f}'

  def __float__(self):
    return float(self._valor)

  def __bool__(self):
    if self._valor > 0:
      return True
    return False

drex = Drex(5)
print(float(drex))
print(bool(drex))
drex = Drex(0)
print(bool(drex))

# ## __repr__

# O método mágico __repr__ serve para definir como o objeto será representado oficialmente no Python, ou seja, o que aparece quando a gente chama repr(obj) ou simplesmente digita o nome do objeto no console (fora de um print()).

# A ideia do __repr__ é dar uma descrição precisa e útil do objeto, que ajude a debugar e até reconstruir o objeto, se possível.

# > Uma boa prática é que __repr__ retorne uma string que poderia ser usada para recriar o objeto, como: Drex(10).

class Drex:
  def __init__(self, valor):
    self._valor = valor

  def __str__(self):
    arredondado = round(self._valor, 2)
    return f'R$ {arredondado:.2f}'

  def __float__(self):
    return float(self._valor)

  def __bool__(self):
    if self._valor > 0:
      return True
    return False

  def __repr__(self):
    return f"Drex({self._valor})"

d = Drex(7.89)

print(d)       # Usa __str__ → R$ 7.89
print(repr(d)) # Usa __repr__ → Drex(7.89)

# Usamos o __str__ para tornar o objeto legível para humanos.
# Usamos o __repr__ para a representação oficial e para debug do objeto.

### Importância de definir o __repr__:

# Quando colocamos objetos dentro de uma list, dict, set ou qualquer estrutura de dados, o Python não usa o __str__ para exibir cada item, ele usa o __repr__.

carteira = [Drex(10), Drex(7.5), Drex(3.25)]

print(carteira)

########################################################################################################

# ## Métodos aritméticos

# # Vamos considerar a seguinte operação matemática:

# d1 = Drex(3)
# d2 = Drex(1.5)

# soma = d1 + d2

# - Métodos aritméticos definem como o objeto deve agir caso receba uma operação com os sinais aritméticos: `+`, `-`, `*`, `/`, `%`, etc
# - Ex:
# - - Números: realiza a soma
# - - Strings: realiza a concatenação

print(2+3)
print('conca'+'tenação')
print([2]+[3])


# ### __add__

# - Na operação `instancia_1 + instancia_2`, o python interpreta como `instancia1.__add__(instancia2)`

# d1 = Drex(2)
# d2 = Drex(3)
# print(d1+d2) # da erro pois o programa não sabe o que fazer com o sinal de +

class Drex:
    def __init__(self, valor):
        self._valor = valor

    def __str__(self):
        arredondado = round(self._valor, 2)
        return f'R$ {arredondado:.2f}'
    
    def __float__(self):
        return float(self._valor)
    
    def __bool__(self):
        if self._valor > 0:
            return True
        return False

    def __repr__(self):
      return f"Drex({self._value})"
    
    def __add__(self, x: Drex):
      soma = self._valor + x._valor
      return Drex(soma)

    def __sub__(self, x):
        return Drex(self._valor - x._valor)

d1 = Drex(5)
d2 = Drex(3.6)
print(d1 + d2)

d3 = Drex(5)
d4 = Drex(3.6)
print(d3-d4)

# Outras operações matemáticas que podem ser implementadas com métodos mágicos:

# __sub__ : subtração (-)
# __mul__ : multiplicação (*)
# __truediv__ : divisão real (/)
# __floordiv__ : divisão inteira (//)
# __mod__ : resto da divisão (%)

########################################################################################################

## Métodos de comparação

### __eq__ (igual, ==)

# Da mesma forma que o método mágico `__add__` "ensina" o python como lidar com o sinal de adição, o método mágico `__eq__` "ensina" o programa a como se comportar caso seja passado o operador igual a, `==` para comparar duas classes.

# O mesmo vale para outras operçaões de comparação, como `>`, `<`, `>=`, `<=`, etc

class Drex:
  def __init__(self, valor):
    self._valor = valor

  def __str__(self):
    arredondado = round(self._valor, 2)
    return f'R$ {arredondado:.2f}'
    
  def __float__(self):
    return float(self._valor)
    
  def __bool__(self):
    if self._valor > 0:
        return True
    return False

  def __repr__(self):
    return f"Drex({self._value})"

  def __add__(self, x):
    soma = self._valor + x._valor
    return Drex(soma)

  def __eq__(self, x):
    return self._valor == x._valor

d1 = Drex(3)
d2 = Drex(1.5)

print(d1 == d2)

d3 = Drex(2)
d4 = Drex(2)
print(d3 == d4)
# print(d3 > d4)

# Outras operações de comparação que podem ser implementadas com métodos mágicos:

# __gt__ : greater than/maior que (>)
# __ge__ : greater or equal/maior ou igual (>=)
# __lt__ : less than/menor que (<)
# __le__ : less or equal/menor ou igual (<=)
# __ne__ : not equal/diferente (!=)

# ### __hash__ (hash de objetos)

# Em Python, o método mágico `__hash__` é utilizado quando um objeto precisa ser usado em estruturas de dados baseadas em hash, como **dicionários** ou **conjuntos** (set).


# Estruturas de dados baseadas em hash são estruturas que usam um "código único" (chamado hash) para guardar e buscar informações de forma muito rápida.

# Por exemplo, tentem pensar em um armário com várias gavetas.
# Cada vez que queremos guardar algo (como uma chave ou camiseta), usamos uma função hash para descobrir em qual gaveta aquilo deve ficar.

# Quando precisar buscar depois, é só calcular o hash de novo — e pronto, já sabe a gaveta certa!


# Assim como o `__eq__` "ensina" ao Python como comparar dois objetos com ==, o `__hash__` diz ao Python **como calcular um valor hash** para aquele objeto. Esse valor precisa ser **imutável**, ou seja, se o conteúdo do objeto não muda, o valor do hash também não pode mudar.

# Obs: Para que um objeto possa ser usado como chave em um dict ou membro de um set, ele **precisa implementar** tanto `__eq__` quanto `__hash__`.

class Drex:
  def __init__(self, valor):
    self._valor = valor

  def __str__(self):
    arredondado = round(self._valor, 2)
    return f'R$ {arredondado:.2f}'

  def __float__(self):
    return float(self._valor)

  def __bool__(self):
    return self._valor > 0

  def __repr__(self):
    return f"Drex({self._value})"

  def __add__(self, x):
    soma = self._valor + x._valor
    return Drex(soma)

  def __eq__(self, x):
    return self._valor == x._valor

  def __hash__(self):
    valor_hash = hash(self._valor)
    return valor_hash # Usa o hash interno do número

d1 = Drex(10)
d2 = Drex(10)
d3 = Drex(5)

# Mesmo valor, considerados iguais, e hash igual
print(d1 == d2)           # True
print(hash(d1), hash(d2)) # Hashes iguais

# Dicionário com objetos Drex como chave
carteira = {d1: 'Saldo principal', d3: 'Saldo reserva'}

print(carteira[d1])  # Saldo principal
print(carteira[d3])  # Saldo reserva

# Se o método `__hash__` não for implementado, ao tentar usar o objeto como chave num dicionário, o Python vai lançar um erro do tipo

# ```python
# TypeError: unhashable type: 'Drex'
# ```


# E se fizessemos o print abaixo, o que aconteceria?

print(carteira[d2])
# O hash do d2 é o número 10. No dicionário, o hash com o número 10 traz o valor 'Saldo principal'. O python não sabe que o nome das variáveis são diferentes, ele sabe o hash armazenado e o valor que ele carrega. Por isso que ao usar o print(carteira[d2]) ele traz o valor de carteira[d1]

########################################################################################################

# Nesses sites aqui vocês podem ver uma lista dos principais métodos mágicos e suas utilizações

# https://www.tutorialsteacher.com/python/magic-methods-in-python

# https://rszalski.github.io/magicmethods/