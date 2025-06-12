# # Atributos estáticos

# - Atributo que pertence à classe, e não ao objeto instanciado daquela classe. 

# Chamado também de:
# - `atributo de classe` ou `variável de classe`

# - Declarado diretamente na classe

# ```python
# class Teste:
#     atributo_estatico = 'nome'
# ```

# - Acessível independente de instâncias da classe

# Sintaxe para uso:

# ```python
# nome_da_classe.nome_do_atributo
# ```

# Exemplo de uso: Controle dos CPFs já cadastrados

from datetime import date
from typing import List

class Titular:
    cpfs_utilizados: List[str] = []
    def __init__(self, nome: str, cpf: str, dt_nasc: date):
        self._nome: str = nome
        self._cpf: str = cpf
        self._dt_nasc: date = dt_nasc
        Titular.cpfs_utilizados.append(cpf)

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
    def data_nascimento(self) -> date:
        return self._dt_nasc


dt_nasc = date(year=1991, month=8, day=6)
t1 = Titular(nome='Pedro', cpf='40040040047', dt_nasc=dt_nasc)
print(Titular.cpfs_utilizados)

t2 = Titular(nome='Maria', cpf='40040040047', dt_nasc=dt_nasc)
print(Titular.cpfs_utilizados)


# Como controlar efetivamente os CPFs?

# Opção 1:
# - Validar os CPFs no nosso programa principal

cpf = '40040040048'
if cpf in Titular.cpfs_utilizados:
    print('CPF já cadastrado')
else:
    dt_nasc = date(year=1991, month=8, day=6)
    t1 = Titular(nome='Pedro', cpf=cpf, dt_nasc=dt_nasc)

print(Titular.cpfs_utilizados)

# Opção 2:
# - Validar o CPF no construtor da classe Titular:

from datetime import date
from typing import List

class Titular:
    cpfs_utilizados: List[str] = []
    def __init__(self, nome: str, cpf: str, dt_nasc: date):
        if cpf in Titular.cpfs_utilizados:
            print('CPF já cadastrado: ', cpf)
            return
        self._nome: str = nome
        self._cpf: str = cpf
        self._dt_nasc: date = dt_nasc
        Titular.cpfs_utilizados.append(cpf)
        
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
    def data_nascimento(self) -> date:
        return self._dt_nasc

cpf1 = '40040040047'
dt_nasc = date(year=1991, month=8, day=6)

t1 = Titular(nome='Isabela', cpf=cpf1, dt_nasc=dt_nasc)
t2 = Titular(nome='Andre', cpf=cpf1, dt_nasc=dt_nasc)

cpf2 = '40040040048'
t3 = Titular(nome='Malu', cpf=cpf2, dt_nasc=dt_nasc)

print(t1.nome_titular)
# print(t2.nome_titular) # t2 não é criado, pois cpf já existe
print(t3.nome_titular)
print(Titular.cpfs_utilizados)
a = 2

# Problema!!!

# Uso do nome da classe. Em casos de refatoração, como fazer?

# ```python
# nome_da_classe.nome_do_atributo
# ```

########################################################################################################

# # Métodos de classe

# - Método que pertence à classe, e recebe a classe como parâmetro: `cls`

# Declarado da seguinte forma:

# ```python
# @classmethod
# def metodo_de_classe(cls, parametros):
# ```

# > Importante: nos métodos de classe passamos a referência à classe usando normalmente o `cls`

# &nbsp;

# Sintaxe para uso:

# ```python
# instancia_do_objeto.nome_do_metodo_da_classe()
# ```

# Exemplo de uso: Controle dos CPFs já cadastrados

from datetime import date
from sys import exception
from typing import List

class Titular:
    cpfs_utilizados: List[str] = []
    def __init__(self, nome: str, cpf: str, dt_nasc: date):
        if self.cpf_ja_utilizado(cpf):
            return
        self._nome: str = nome
        self._cpf: str = cpf
        self._dt_nasc: date = dt_nasc
        self.adicionar_cpf(cpf)
    
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
    def data_nascimento(self) -> date:
        return self._dt_nasc
    
    @classmethod
    def cpf_ja_utilizado(cls, cpf: str) -> bool:
        if cpf in cls.cpfs_utilizados:
            print('CPF já cadastrado: ', cpf)
            return True
        return False

    @classmethod
    def adicionar_cpf(cls, cpf):
        cls.cpfs_utilizados.append(cpf)

    @classmethod
    def listar_cpfs(cls):
      print(cls.cpfs_utilizados)


cpf = '12345678900'
dt_nasc = date(year=1991, month=8, day=6)
t1 = Titular('Pedro', cpf, dt_nasc)
t1.listar_cpfs()

print()
cpf = '98765432100'
dt_nasc = date(year=1995, month=6, day=20)
t2 = Titular('Laura', cpf, dt_nasc)

t2.listar_cpfs()

########################################################################################################

# Métodos estáticos

# - Método que não deveria afetar o estado do objeto e nem da classe.
# - Poderia estar fora da classe, mas por conveniência (já que normalmente envolve "assuntos" da classe) fica dentro dela.

# Declarado da seguinte forma: 

# ```python
# @staticmethod
# def metodo_estatico(parametros):
# ```

# > Importante: nos métodos estáticos, não passamos a referência ao objeto `self` e nem a referência da classe `cls`


# Sintaxe para uso:

# ```python
# nome_da_classe.nome_do_metodo(parametros)
# ```

# Exemplo de uso: Validação de CPF

from datetime import date
from sys import exception
from typing import List

class Titular:
    cpfs_utilizados: List[str] = []
    def __init__(self, nome: str = None, cpf: str = None, dt_nasc: date = None):
        if self.cpf_ja_utilizado(cpf):
            return
        else:
            self.adicionar_cpf(cpf)
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
    def data_nascimento(self) -> date:
        return self._dt_nasc

    @classmethod
    def cpf_ja_utilizado(cls, cpf: str) -> bool:
        if Titular.validar_cpf(cpf) and cpf in cls.cpfs_utilizados:
            print('CPF já cadastrado: ', cpf)
            return True
        return False

    @classmethod
    def adicionar_cpf(cls, cpf):
        cls.cpfs_utilizados.append(cpf)
    
    @classmethod
    def listar_cpfs(cls):
      print(cls.cpfs_utilizados)
    
    @staticmethod
    def validar_cpf(cpf: str):
        if cpf and len(cpf) == 11:
            return True
        else:
            return False


# cpf1 = '40040040047'
# dt_nasc = date(year=1991, month=8, day=6)
# t1 = Titular(nome='Pedro', cpf=cpf1, dt_nasc=dt_nasc)

cpf2 = '40040040983'
print(Titular.validar_cpf(cpf2))
cpf3 = '400400409883'
print(Titular.validar_cpf(cpf3))