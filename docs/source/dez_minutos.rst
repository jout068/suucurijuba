.. _modulo_dez_um:

.. include:: special.rst

Aprenda Python em dez minutos I
===============================

Vamos nos concentrar no Python 3, pois essa é a versão que você deve usar.
Todos os exemplos do livro estão em Python 3, e se alguém aconselhar você a usar 2,
não é seu amigo.

Propriedades
------------
Python é fortemente tipado (ou seja, os tipos são impostos), dinamicamente,
implicitamente tipado (ou seja, você não precisa declarar variáveis),
sensível a maiúsculas (ou seja, var e VAR são duas variáveis diferentes)
e orientado a objetos (ou seja, tudo é um objeto) .

Conseguindo ajuda
-----------------

A ajuda em Python está sempre disponível diretamente no interpretador.
Se você quiser saber como um objeto funciona, tudo o que você precisa fazer
é chamar help(<object>)! Também são úteis dir(), que mostra todos os métodos do objeto,
e <object>.__doc__, que mostra sua string de documentação:

>>> help(5)
Ajuda no objeto int:
(etc etc)

>>> dir(5)
['__abs__', '__adicionar__', ...]

>>> abs.__doc__
'abs(número) -> número

Retorna o valor absoluto do argumento.

Sintaxe
-------

O Python não possui caracteres de terminação de instrução obrigatórios e os blocos
são especificados por recuo. Recuar para iniciar um bloco, recuar para terminar um.
As instruções que esperam um nível de recuo terminam em dois pontos (:red:`:`).
Os comentários começam com o sinal de sustenido (:red:`#`) e são strings de linha única
e várias linhas são usadas para comentários de várias linhas. Os valores são atribuídos
(na verdade, os objetos são vinculados a nomes) com o sinal de igual (“:red:`=`”),
e o teste de igualdade é feito usando dois sinais de igual (“:red:`==`”).
Você pode incrementar/diminuir valores usando os operadores :red:`+=` e :red:`-=` respectivamente
pelo valor do lado direito. Isso funciona em muitos tipos de dados, incluindo strings.
Você também pode usar várias variáveis em uma linha. Por exemplo:

.. code-block:: python

    >>> myvar = 3
    >>> myvar += 2
    >>> myvar
    5
    >>> myvar -= 1
    >>> myvar
    4
    """Este é um comentário de várias linhas.
     As linhas a seguir concatenam as duas strings."""
    >>> mystring = "Hello"
    >>> mystring += " world."
    >>> print(mystring)
    Hello world.
    # Isso troca as variáveis em uma linha(!).
    # Não viola a tipagem forte porque os valores não são
    # realmente sendo atribuído, mas novos objetos são vinculados a
    # os nomes antigos.
    >>> myvar, mystring = mystring, myvar


.. seealso::
    :ref:`modulo_inicia`

Tipos de dados
--------------

As estruturas de dados disponíveis em python são listas, tuplas e dicionários.
Os conjuntos estão disponíveis na biblioteca de conjuntos
(mas são integrados ao Python 2.5 e posterior). Listas são como arrays unidimensionais
(mas você também pode ter listas de outras listas), dicionários são arrays associativos
(também conhecidos como tabelas de hash) e tuplas são arrays unidimensionais imutáveis
(os “arrays” do Python podem ser de qualquer tipo, então você pode misturar,
por exemplo, inteiros, strings, etc em listas/dicionários/tuplas).
O índice do primeiro item em todos os tipos de array é 0.
Números negativos contam do final para o início, -1 é o último item.
Variáveis podem apontar para funções. O uso é o seguinte:

>>> sample = [1, ["another", "list"], ("a", "tuple")]
>>> mylist = ["List item 1", 2, 3.14]
>>> mylist[0] = "List item 1 again" # We're changing the item.
>>> mylist[-1] = 3.21 # Here, we refer to the last item.
>>> mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14}
>>> mydict["pi"] = 3.15 # This is how you change dictionary values.
>>> mytuple = (1, 2, 3)
>>> myfunction = len
>>> print(myfunction(mylist))
3

Você pode acessar intervalos de array usando dois pontos (:red:`:`).
Deixar o índice inicial vazio assume o primeiro item, deixando o índice final assume o último item.
A indexação é inclusiva-exclusiva, portanto, especificar :red:`[2:10]` retornará os itens [2]
(o terceiro item, devido à indexação 0) a [9] (o décimo item), inclusive (8 itens).
Índices negativos contam do último item para trás (portanto -1 é o último item) assim:

>>> mylist = ["List item 1", 2, 3.14]
>>> print(mylist[:])
['List item 1', 2, 3.1400000000000001]
>>> print(mylist[0:2])
['List item 1', 2]
>>> print(mylist[-3:-1])
['List item 1', 2]
>>> print(mylist[1:])
[2, 3.14]
# Adicionando um terceiro parâmetro, "step" terá o passo do Python em
# N incrementos de itens, em vez de 1.
# Por exemplo, isso retornará o primeiro item, depois irá para o terceiro e
# retorna isso (portanto, itens 0 e 2 na indexação 0).>>> print(mylist[::2])
['List item 1', 3.14]

Strings
-------

Suas strings podem usar aspas simples ou duplas, e você pode ter aspas
de um tipo dentro de uma string que usa o outro tipo (ou seja, "He said 'hello'." é válido).
Strings de várias linhas são colocadas entre _aspas duplas triplas (ou simples)_ (:red:`“”“`).
As strings do Python são sempre Unicode, mas há outro tipo de string que é bytes puros.
Esses são chamados de bytestrings e são representados com o prefixo :red:`b`,
por exemplo :red:`b'Hello \xce\xb1'`. . Para preencher uma string com valores,
você usa o operador :red:`%` (módulo) e uma tupla. Cada :red:`%s` é substituído por um item da tupla,
da esquerda para a direita, e você também pode usar substituições de dicionário, assim:

>>> print("Nome: %s\
Número: %s\
String: %s" % (myclass.name, 3, 3 * "-"))
Nome: Stavros
Número: 3
String: ---

strString = """Isso é
uma string multilinha
"""

# AVISO: Cuidado com os s finais em "%(key)s".
>>> print("Este %(verbo)s é um %(substantivo)s." % {"substantivo": "teste", "verbo": "é"})
Isto é um teste.

>>> nome = "Stavros"
>>> "Olá, {}!".format(name)
Olá, Stavros!
>>> print(f"Olá, {nome}!")
Olá, Stavros!

Declarações de controle de fluxo
--------------------------------

As instruções de controle de fluxo são :red:`if`, :red:`for` e :red:`while`.
Use for para enumerar os membros de uma lista.
Para obter uma lista de números, use :red:`range(<number>)`.
A sintaxe dessas declarações é assim:

.. code-block:: python

    rangelist = range(10)
    >>> print(rangelist)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for número in rangelist:
        # Verifique se o número é um dos
        # os números na tupla.
        if número in (3, 4, 7, 9):
            # "Break" termina um for sem
            # executar a cláusula "else".
            break
        else:
            # "continue" inicia a próxima iteração
            # do laço. É bastante inútil aqui,
            # pois é a última instrução do loop.
            continue
    else:
        # A cláusula "else" é opcional e é
        # executado apenas se o loop não "quebrar".
        pass # Não faça nada

    if rangelist[1] == 2:
        print("O segundo item (as listas são baseadas em 0) é 2")
    elif rangelist[1] == 3:
        print("O segundo item (as listas são baseadas em 0) é 3")
    else:
        print("Não sei")

    while rangelist[1] == 1:
        pass

Funções
-------

As funções são declaradas com a palavra-chave :red:`def`.
Os argumentos opcionais são definidos na declaração da função após os argumentos obrigatórios,
recebendo um valor padrão. Para argumentos nomeados, o nome do argumento recebe um valor.
As funções podem retornar uma tupla (e usando a descompactação da tupla,
você pode efetivamente retornar vários valores).
As funções lambda são funções ad hoc compostas por uma única instrução.
Os parâmetros são passados por referência, mas os tipos imutáveis (tuplas, ints, strings, etc)
não podem ser alterados no chamador pelo chamado. Isso ocorre porque apenas o local de memória
do item é passado e vincular outro objeto a uma variável descarta o antigo, portanto,
os tipos imutáveis são substituídos. Por exemplo:

.. code-block:: python

    # O mesmo que def funcvar(x): return x + 1
    funcvar = lambda x: x + 1
    >>> print(funcvar(1))
    2

    # an_int e a_string são opcionais, eles possuem valores padrão
    # se um não for passado (2 e "Uma string padrão", respectivamente).
    def passing_example(a_list, an_int=2, a_string="Uma string padrão"):
        a_list.append("Um novo item")
        an_int = 4
        return a_list, an_int, a_string

    >>> minha_lista = [1, 2, 3]
    >>> meu_int = 10
    >>> print(passing_example(my_list, my_int))
    ([1, 2, 3, 'Um novo item'], 4, "Uma string padrão")
    >>> minha_lista
    [1, 2, 3, 'Um novo item']
    >>> meu_int
    10

Exercícios para este capítulo
-----------------------------

Agora você pode tentar os exercícios em:
    :ref:`modulo_dojo_zero`

.. note::
   Procure ser cooperativo com a sua equipe.
