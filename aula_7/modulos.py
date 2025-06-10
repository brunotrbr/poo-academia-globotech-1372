# # Módulos, pacotes e bibliotecas

# Por enquanto, podemos dizer que uma biblioteca nada mais é que **uma coleção de funcionalidades prontas**

# Por exemplo: datetime, random, etc.

# ## Importando bibliotecas

# Para importar uma biblioteca usamos a sintaxe: 

# import nome_da_biblioteca

import random

random.randint(0,100)

# Porém, pode acontecer de o nome da biblioteca ser muito grande ou até mesmo conflitar com o nome de uma variável que já existe no nosso código.
# Por exemplo, se quisermos usar a biblioteca "datetime" e já tivermos uma variável chamada "datetime", teremos um conflito de nomes.

# Para resolver esse tipo de problema, podemos usar um "apelido" para a biblioteca, que em python é chamado de "alias".

# ## Importando bibliotecas: alias

# Para isso, usamos a sintaxe: 

# import nome_da_biblioteca as apelido_da_biblioteca

# Assim, quando formos nos referir à biblioteca para utilizar uma de suas funções, usamos o seu apelido

import random as rd

rd.randint(0, 100)

# Mas ainda existe um problema nessa abordagem. Estamos importando a biblioteca inteira, mas talvez não precisemos de todas as suas funcionalidades.

# O que fazer? Importar somente o que precisamos!


# ## Importando parcialmente as bibliotecas

# Para isso usamos a sintaxe:

# from nome_da_biblioteca import nome_da_funcao_ou_classe (as alias_da_funcao)

# Obs: O alias é opcional.

from random import randint as rdint, random as rd

print(rdint(1,100))
print(rd()) # gera um float entre 0 e 1

# Importante: cuidado para não sobrescrever uma função já existente
def random():
    return print('Olá')

print(rdint(1,100))
random() # sobrescrevi a função random com um print
print(rd()) # gera um float entre 0 e 1

help(random)

import random
print(random.randint(1,10))

def random():
    return print('Olá 2')

# print(random.randint(1,100)) # Da erro 'function' object has no attribute 'randint' porque sobrescrevemos a biblioteca random com o def da função random.

def rd():
    return print("Método rd")

print(rd())
rd()

# def metodo_sem_retorno(): O método não deve retornar nada
def metodo_sem_retorno() -> None: #  O método não deve retornar nada
    print('metodo_sem_retorno')

def metodo_retorna_bool() -> bool:
    return True

def rd():
    return print('Metodo rd')

variavel_sem_retorno = metodo_sem_retorno()
variavel_bool = metodo_retorna_bool()
variavel_rd = rd()
print(rd())

a = 2
# ## Módulos

# Qualquer script Python (arquivo com extensão .py) pode ser considerado um módulo.

# Motivação para usar módulos: modularização e organização.


# ##  Pacotes

# Pacotes são uma forma de organizar módulos em diretórios. Um pacote é um diretório que contém um arquivo especial chamado `__init__.py`, que pode estar vazio ou conter código de inicialização do pacote.

# Motivação para usar pacotes: Agrupar conjuntos de módulos com funcionamento semelhante e/ou complementar

# Exemplo de pacote: a biblioteca `os`, que contém módulos para interagir com o sistema operacional.

################ INÍCIO da explicação do __init__

# ## O que é o __init__.py

# Imagine que você tem uma pasta cheia de arquivos Python, e essa pasta é um "pacote" com códigos que trabalham juntos.
# O arquivo `__init__.py` é como um cartão de visita que diz:

# > “Ei, Python! Essa pasta aqui é um pacote de código que pode ser usado em outros lugares.”

# Sem esse arquivo (em versões antigas do Python), o Python nem reconheceria a pasta como um pacote.

# Pensem em um estojo de lápis. Dentro do estojo você tem:
# - Um lápis
# - Uma borracha
# - Um apontador

# Agora imaginem que vocês tem uma pasta chamada estojo, e dentro dela:

# ```
# estojo/
# |-- __init__.py
# |-- lapis.py
# |-- borracha.py
# |-- apontador.py
# ```

# Se vocês quiserem usar os itens do estojo em outro lugar do seu código, vocês fazem algo assim:

# from estojo import lapis

# # ou

# from estojo import borracha

# Importando a classe Lapis e Borracha diretamente
from estojo import Lapis
from estojo import Borracha

lapis = Lapis()
lapis.escrever('olá')
lapis.desenhar()

borracha = Borracha()
borracha.apagar()
a = 2

# Importando as funções escrever e apagar
from estojo import escrever, apagar

escrever("teste")
apagar()
a = 2

# O __init__ não bloqueia a importação da classe Lapis 
from estojo import lapis
lapis._desenhar()
a = 2


# O Python só entende que a pasta estojo é um pacote porque tem o `__init__.py` lá dentro. Ele marca a pasta como um pacote de verdade.

# ### Como podemos usar o \_\_init\_\_.py?
# Além de ser esse “sinalizador”, o `__init__.py` também pode:

# 1. Executar código automaticamente quando o pacote for importado.
# 2. Organizar o que vai estar disponível no pacote.

# para demonstrar isso, vamos criar a estrutura descrita acima:

# # ```
# arquivo __init__.py
# from .lapis import Lapis
# from .borracha import Borracha
# from .apontador import Apontador

# print("Importando o estojo...")

# # Cria funções que usam apenas os métodos que queremos expor
# lapis = Lapis()
# escrever = lapis.escrever

# borracha = Borracha()
# apagar = borracha.apagar

# apontador = Apontador()
# apontar = apontador.apontar

# arquivo lapis.py
# class Lapis:
#     def escrever(self, texto):
#         print(f"Escrevendo: {texto}")

#     def desenhar(self):
#         print("Fazendo um desenho com o lápis...")

# arquivo borracha.py
# class Borracha:
#     def apagar(self):
#         print("Apagando o que foi escrito...")

# arquivo usar_estojo.py
# # Exemplo em que o lapis é exposto diretamente.
# from estojo import Lapis, Borracha

# lapis = Lapis()
# borracha = Borracha()

# lapis.escrever("Olá, mundo!")
# lapis.desenhar()
# borracha.apagar()

# # Exemplo em que o desenhar não é exposto diretamente.
# from estojo import escrever, apagar  # desenhar não está acessível diretamente

# escrever("Python é massa!")
# apagar()

# # # Se tentar usar desenhar():
# from estojo import lapis
# lapis.desenhar()  # Vai dar erro, porque 'desenhar' não foi exposto?
##

# ```

# Mesmo que no `__init__.py` a gente exponha só o escrever, isso não bloqueia o acesso ao módulo inteiro (como lapis.py). Ou seja:

# O `__init__.py` serve para facilitar a importação, não para esconder código.

# Ele não restringe o acesso aos arquivos internos do pacote.

# Se lapis.py está no pacote, qualquer um pode importá-lo diretamente.

# Para "esconder" algo, seguimos a convenção de colocar "_" antes do nome do método, como por exemplo `_desenhar()`, para que quem for usar o lápis evite de chamar o método diretamente.

################ FIM da explicação do __init__

# ##  Bibliotecas

# No uso coloquial, muitas vezes chamamos módulos e pacotes de "bibliotecas". E, coloquialmente, este uso é bem aceitável.

# Mas, formalmente falando, usamos o termo **biblioteca** para nos referir a pacotes (ou até mesmo módulos individuais) que são publicados, como parte de um projeto particular, ou para determinado uso.

# Em resumo,

# - Um **módulo** é um arquivo de extensão .py com código em Python nele (comumente definição de funções, classes, etc.);

# - Um **pacote** é uma coleção de módulos. Costuma ser uma pasta com os módulos e o arquivo especial \_\_init\_\_.py vazio;

# - Uma **biblioteca** é uma coleção de pacotes ou módulos.

## Criando e importando nossos próprios modulos/pacotes/bibliotecas

# Inicialmente vamos criar a pasta `modulos_e_pacotes` fora das nossas estrutuas de pastas das aulas. Dentro dela, vamos criar a pasta `biblioteca_contas` e dentro dela a pasta `pacote_titulares`.

# No momento teremos a seguinte estrutura:

# aula_5
# aula_6
# aula_7
# |- modulos_metodos_magicos.py
# ...
# modulos_e_pacotes
# |- __init__.py
# |- biblioteca_contas
# |--- __init__.py
# |--- pacote_titulares
# |----- __init__.py
# |----- modulo_titular.py


# Dentro da pasta pacote_titulares vamos adicionar o arquivo `modulo_titular.py`, com o conteúdo da nossa classe Titular.

# Neste momento, o modulo_titular.py é um `módulo`.

# O diretório `pacote_titulares`, por enquanto, é um diretório comum do windows/linux. Ao criarmos o __init__.py dentro dele, ele se transforma em um `pacote`.

# Após esses passos, a nossa estrutura ficou da seguinte forma:

# aula_5
# aula_6
# aula_7
# |- modulos_metodos_magicos.py
# ...
# modulos_e_pacotes
# |- __init__.py
# |- biblioteca_contas
# |--- __init__.py
# |--- pacote_titulares
# |----- __init__.py
# |----- modulo_titular.py

# Agora vamos criar um arquivo chamado `main.py`, importar a classe `Titular` e testar o código, conforme o código abaixo:

from modulos_e_pacotes.biblioteca_contas.pacote_titulares.modulo_titular import Titular

dt_nasc = date(year=1991, month=8, day=6)
t1 = Titular('Pedro', 'Cientista de dados', dt_nasc)
print(t1.nome_titular)
print(t1.cpf)
print(t1.data_nascimento)

# O erro

# Exception has occurred: ModuleNotFoundError
# No module named 'modulos_e_pacotes'
#   File "<caminho_do_script>/modulos_metodos_magicos.py", line 131, in <module>
#     from modulos_e_pacotes.biblioteca_contas.pacote_titulares.modulo_titular import Titular
# ModuleNotFoundError: No module named 'modulos_e_pacotes'

# Acontece porque quando importamos um pacote, o python procura ele nos diretórios existentes em `sys.path`.

# Nesse caso, como é um pacote nosso que está sendo adicionado manualmente, precisamos incluir ele no sys.path. Caso contrário, o programa vai dar erro.

# Para solucionar isso precisamos realizar duas configurações:
# - Adicionar a pasta `modulos_e_pacotes` no `sys.path`
# - Definir o local de execução do nosso arquivo python utilizando a variável de ambiente `PYTHONPATH`

# ## Adicionando a pasta no sys.path

# # Vamos voltar no código do arquivo `main.py` e antes de fazer o import `from modulos_e_pacotes.biblioteca_contas.pacote_titulares.modulo_titular import Titular` vamos incluir as seguintes linhas: 

# import sys
# import os

# module_path = os.path.abspath('modulos_e_pacotes')
# sys.path.append(module_path) # append no final do sys.path
# # sys.path.insert(0, module_path) # insere na posição 0 do sys.path

import sys
import os

module_path = os.path.abspath('modulos_e_pacotes')
sys.path.append(module_path) # append no final do sys.path
# sys.path.insert(0, module_path) # insere na posição 0 do sys.path

from modulos_e_pacotes.biblioteca_contas.pacote_titulares.modulo_titular import Titular
from datetime import date

dt_nasc = date(year=1991, month=8, day=6)
t1 = Titular('Tales', 'Cientista de dados', dt_nasc)
print(t1.nome_titular)
print(t1.cpf)
print(t1.data_nascimento)

# ## Definindo o local de execução

# No vscode, precisamos incluir o arquivo `launch.json` com o seguinte conteúdo:
# ```json
# {
#     "version": "0.2.0",
#     "configurations": [
#         {
#             "name": "Python: Current File",
#             "type": "python",
#             "request": "launch",
#             "program": "${file}",
#             "console": "integratedTerminal",
#             "cwd": "${fileDirname}",
#             "env": {"PYTHONPATH": "${workspaceFolder}${pathSeparator}${env:PYTHONPATH}"}
#         }
#     ]
# }
# ```
# E usar o `Python: Current File` para rodar o debugger.

# Agora conseguimos rodar o programa

# Após executar o programa, vamos modularizar a parte de contas.

# Dentro de `modulos_e_pacotes/biblioteca_contas` vamos criar uma nova pasta chamada `pacote_contas` e dentro dela os arquivos `modulo_contabase.py`, `modulo_corrente.py` e `modulo_poupanca.py`, cada um com seu respectivo código. também criaremos o arquivo `__init__.py`, permitindo apenas o uso da `ContaCorrente` e da `ContaPoupanca`
 
# Com isso teremos a seguinte estrutura:

# aula_5
# aula_6
# aula_7
# |- modulos_metodos_magicos.py
# ...
# modulos_e_pacotes
# |- __init__.py
# |- biblioteca_contas
# |--- __init__.py
# |--- pacote_titulares
# |----- __init__.py
# |----- modulo_titular.py
# |--- pacote_contas
# |----- __init__.py
# |----- modulo_contabase.py
# |----- modulo_corrente.py
# |----- modulo_poupanca.py

# TODO:
# Importar conta corrente e conta poupança no arquivo `main.py`
# Criar uma conta corrente e uma conta poupança
# Testar as operações

from modulos_e_pacotes.biblioteca_contas.pacote_contas import ContaCorrente, ContaPoupanca

cc1 = ContaCorrente(t1, '001', 'c101')
cc1.deposito(180.50) # nesse ponto eu estou informando que o depósito vai ser feito para a cc1
print(cc1.saldo)
cc1.saque(100)
print(cc1.saldo)
cc1.pagamento(80.0)
print(cc1.saldo)

cc1.extrato()

dt_nasc = date(year=1991, month=8, day=6)
t2 = Titular('Malu', 'Engenheira de dados', dt_nasc)
print(t2.nome_titular)
print(t2.cpf)
print(t2.data_nascimento)

cc2 = ContaCorrente(t2, '001', 'c202')
print(cc2.agencia)
print(cc2.conta)
print(cc2.saldo)
print(cc2.titular.nome_titular)
print(cc2.titular.cpf)
print(cc2.titular.data_nascimento)

cc1.saque(100)
cc1.pagamento(100)
cc1.transferencia(100, cc2)
cc1.deposito(100)
print(cc1.saldo)
cc1.transferencia(100, cc2)
print(cc1.saldo)
print(cc2.saldo)

print()

cc1.extrato()

print()

cc2.extrato()