# ## Recapitulando Introdução à Programação Orientada a Objetos

# # Programação Orientada a Objetos
# - Foco em modelar o mundo real, ou seja, representar coisas do mundo real
# - Descrição de entidades com características, habilidades e ações
# - O programa surge da interação entre esses modelos
# - Amplamente utilizado no desenvolvimento de sistemas


# # Benefícios da POO
# - Facilidade em reutilizar as entidades para resolver problemas semelhantes
# - Facilidade para incorporar o código em outros projetos


# # Mas o que são objetos?
# - Entidades que compões um programa
# - Cada objeto é responsável por executar determinadas tarefas
# - O conjunto de tarefas define seu comportamento


# # Características, estado e funções
# - Representações lógicas de objetos do mundo real, com características, estados e funções
# - As características são chamadas de atributos ou propriedades
# - O estado pode ser entendido como uma característica (ou um conjunto de características) mais flexíveis
# - Funções são ações que o objeto pode realizar


# # Objetos são reais ou abstratos?
# - Objetos podem ser representações reais (pessoas) ou abstratas (departamento de TI)


# ## Praticando um pouco
# # Exercício 1
# Pensando nos conceitos de estado e função mencionados acima, descreva um portão de garagem:

# # Exercício 2
# Pensando nos conceitos de estado e função mencionados acima, descreva uma carro:


# # Com base nos exercícios, podemos observar que:
# Mesmo comportamento + mesma estrutura = mesma categoria ou classe de objeto

#######################################################################################################

# ## Princípios Básicos da POO

# Dentro da POO temos algumas diretrizes que são a base de qualquer linguagem que implementa a orientação a objetos. São esses os pilares:

# - Abstração
# - Encapsulamento
# - Herança
# - Polimorfismo

# ### Abstração
# - Modelar e representar objetos ou conceitos do mundo real
# - Foco nos comportamentos e características essenciais para aquele contexto, e ignorar detalhes irrelevantes. 
# - Não precisamos saber como exatamente funciona internamente, apenas sabemos que funciona. 

# exemplo de um método para passar café com abstração
def fazer_cafe():
  # retorna o café pronto
  pass

# exemplo de um método para passar café sem abstração
def fazer_cafe():
  # adicionar a aǵua fria na chaleira
  # ferver a água
  # pega uma xícara, um coador, o filtro de café, e o pó de café
  # ....
  pass

# E na prática/vida real:


lista = []

for numero in range(1, 11):
    lista.append(numero)

print(lista)

lista.pop(3)
lista.pop(5)

print(lista)


# Sem executar o código acima, conseguimos entender o que vai acontecer, certo?

# Sabemos o que os métodos append e pop fazem? Sim

# Sabemos como o método foi implementado? Não

# Precisamos saber como ele foi implementado? Não

# Em resumo
# Abstração é quando você foca no que importa e esconde os detalhes que não são necessários.
# Você usa uma coisa sem precisar saber como ela funciona por dentro, só precisa saber o que ela faz.
# Facilita a vida do usuário e deixa o sistema mais simples de entender e usar.
# Cria uma interface mais limpa e intuitiva.

# ### Encapsulamento

# - Princípio usado para proteger os dados e controlar como eles são acessados e modificados.
# - Esconder partes internas do funcionamento de um objeto
# - Permitir que ele seja usado de forma segura e controlada.

# - Ajuda a evitar que informações sejam alteradas de qualquer jeito, o que poderia quebrar o funcionamento do programa.

# Imagina que você tem um cofrinho de moedas.
# - Consegue colocar moedas (tem uma entrada).
# - Difícil de mexer nas moedas ou retirar
# - Precisa quebrar o cofrinho ou, em alguns modelos, abrir uma tampa para retirar o dinheiro.

# Isso é encapsulamento.
# O cofrinho protege o dinheiro (os dados) e controla as formas de interagir com ele: você pode adicionar dinheiro, mas não pode mexer diretamente no valor guardado sem seguir um processo controlado.

# Exemplo do código de um cofrinho sem encapsulamento
class Cofrinho:
    def __init__(self):
        self.saldo = 0

cofre = Cofrinho()
cofre.saldo = -100
print(cofre.saldo)


# Exemplo do código de um cofrinho com encapsulamento
class Cofrinho:
    def __init__(self):
        self.__saldo = 0  # __saldo é privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido para depósito.")

    def consultar_saldo(self):
        return self.__saldo

cofre = Cofrinho()
cofre.depositar(50)
cofre.depositar(-20)
print(cofre.consultar_saldo())

# Em resumo

# Encapsulamento serve para proteger os dados.
# Ele esconde o interior dos objetos e permite que você interaja com eles apenas através de métodos (funções) que definem regras e validações.
# Isso deixa seu código mais organizado, seguro e fácil de manter.


# ### Herança

# - Permite que uma classe herde características (atributos) e comportamentos (métodos) de outra classe.
# - Podemos criar uma classe mais genérica (classe pai ou mãe), e depois criar outras classes mais específicas, reaproveitando código repetido.
# - Ajuda a deixar o código mais organizado, mais simples de entender e evita repetições.

# Considerem o conceito de Veículo.
# - Possui elementos comuns a todos os veículos:
# - Tem rodas
# - Pode acelerar
# - Pode frear

# Agora, pensem em veículos mais específicos:
# - Bicicleta → Tem 2 rodas.
# - Carro → Tem 4 rodas e motor.
# - Moto → Tem 2 rodas e motor.

# Esses veículos herdam características e comportamentos do conceito geral de Veículo, mas também podem ter coisas específicas.

# - Uma bicicleta não tem motor, mas um carro tem.

# Exemplo de classe genérica (pai/mãe):

class Veiculo:
    def __init__(self, cor):
        self.cor = cor

    def acelerar(self):
        print("Acelerando...")

    def frear(self):
        print("Freando...")

# Exemplos de classes específicas que herdam de Veiculo:
class Carro(Veiculo):
    def __init__(self, cor, modelo):
        super().__init__(cor)  # Chama o construtor da classe pai
        self.modelo = modelo

    def abrir_porta(self):
        print("Abrindo porta do carro.")

class Bicicleta(Veiculo):
    def __init__(self, cor, marchas):
        super().__init__(cor)
        self.marchas = marchas

    def empinar(self):
        print("Empinando a bicicleta!")

# Exemplo de código usando as classes

carro = Carro("vermelho", "sedan")
carro.acelerar()       # Método herdado
carro.abrir_porta()    # Método próprio

bike = Bicicleta("azul", 21)
bike.acelerar()        # Método herdado
bike.empinar()         # Método próprio

# - As classes Carro e Bicicleta herdam os métodos acelerar() e frear() da classe Veiculo
# - Cada uma pode ter seus próprios métodos específicos, como abrir_porta() no carro e empinar() na bicicleta.

# Em resumo
# - Herança permite que uma classe aproveite atributos e métodos de outra classe mais genérica.
# - Evita repetição de código e organiza melhor as relações entre objetos.
# - As classes filhas podem usar tudo que a classe pai tem e ainda adicionar suas próprias características.


# ### Polimorfismo

# - Se usarmos a herança corretamente, as classes pai e filhos compartilham a maioria dos atributos e propriedades
# - Com isso, podemos usar uma ou outra, na maioria das vezes, com comportamentos diferentes.
# - Capacidade de um mesmo método, com o mesmo nome, se comportar de formas diferentes
# - Polimorfismo vem do grego, e significa "muitas formas".

# - Classes diferentes que estão relacionadas (herança) tenham métodos com o mesmo nome, mas com comportamentos diferentes, cada um adaptado à sua necessidade.

# Vamos pensar no conceito abstrato de "Animal". 
# - Todos os animais emitem som
# - Um cachorro late
# - Um gato mia
# - Uma vaca muge

# - Emitir som é comum para todos, mas cada um faz de um jeito diferente. 

# Isso é polimorfismo: a mesma ação (emitir som), com comportamentos diferentes dependendo do animal.


# Exemplo de classe genérica
class Animal:
    def emitir_som(self):
        print("Som genérico de animal")


# Exemplo de classes específicas que sobrescrevem o método emitir_som:

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

class Vaca(Animal):
    def emitir_som(self):
        print("Muu!")


# Exemplo de polimorfismo na prática

animais = [Cachorro(), Gato(), Vaca()]

for animal in animais:
    animal.emitir_som()


# Mesmo chamando o mesmo método emitir_som(), cada objeto executa um comportamento diferente, de acordo com sua classe específica.


# Exemplo da classe animal sem polimorfismo com ifs:
class Animal:
    def __init__(self, tipo_animal: str):
        self.__animal = tipo_animal
    
    def emitir_som(self):
        if self.__animal == 'cachorro':
            print("Au au!")
        elif self.__animal == 'gato':
            print("Miau!")
        elif self.__animal == 'vaca':
            print("Muu!")
        else:
            print("Animal não identificado!")

# Exemplo da classe animal sem polimorfismo com switch/match:
class Animal:
    def __init__(self, tipo_animal: str):
        self.__animal = tipo_animal
    
    def emitir_som(self):
        match self.__animal:
            case 'cachorro':
                print("Au au!")
                return
            case 'gato':
                print("Miau!")
                return
            case 'vaca':
                print("Muu!")
                return
            case _:
                print("Animal não identificado!")
                return

# - Queremos criar códigos mais genéricos e flexíveis, que funcionam pra vários tipos de objetos diferentes, mas cada um executa sua própria lógica.
# - Evita um monte de if ou switch no código, deixando tudo mais limpo e elegante.

# Em resumo

# Polimorfismo permite que um mesmo método tenha comportamentos diferentes dependendo do objeto.

# É como dizer "faça isso", e cada objeto sabe como fazer do seu jeito.

# Deixa o código mais flexível, limpo e organizado.


# ### Composição de objetos

# - Um objeto pode ser formado por outros objetos.
# - Dizemos que um objeto "tem um" outro objeto, ao invés de "ser um". O "Ser" seria o conceito de herança.
# - Composição é como aquele brinquedo "Lego". A partir de peças pequenas, podemos montar qualquer coisa.
# - Na programação, vamos montar coisas mais complexas a partir de coisas menores. 
# - Criar objetos que trabalham juntos, cada um com sua responsabilidade, deixando o código mais organizado e fácil de entender.

# Pensem numa Casa.
# - Composta por vários objetos:
# - Porta
# - Janela
# - Quarto
# - Cozinha
# - Banheiro

# - A Casa tem uma porta, tem janelas, tem quartos
# - Mas a Casa não É uma porta, nem É uma janela. 
# - Cada objeto existe de forma independente, que formam algo maior.

# Exemplo criando os objetos menores:

class Porta:
    def abrir(self):
        print("Porta aberta.")

    def fechar(self):
        print("Porta fechada.")

class Janela:
    def abrir(self):
        print("Janela aberta.")

    def fechar(self):
        print("Janela fechada.")

# Exemplo da classe Casa usando composição:

class Casa:
    def __init__(self):
        self.porta = Porta()
        self.janela = Janela()

    def abrir_casa(self):
        self.porta.abrir()
        self.janela.abrir()

    def fechar_casa(self):
        self.porta.fechar()
        self.janela.fechar()

# Exemplo usando a composição

minha_casa = Casa()

minha_casa.abrir_casa()
minha_casa.fechar_casa()

# A classe Casa não herda de Porta ou Janela.
# Ela tem uma porta e tem uma janela, e pode usar os métodos desses objetos dentro dos seus próprios métodos.

# Em resumo

# Composição é quando um objeto é formado por outros objetos.

# Representa a relação "tem um".

# Permite criar sistemas mais flexíveis, organizados e modulares.

# Cada objeto cuida de uma responsabilidade específica.
