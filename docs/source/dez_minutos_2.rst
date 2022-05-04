.. _modulo_dez_dois:

.. include:: special.rst

Aprenda Python em dez minutos II
================================

Classes
-------

Python suporta uma forma limitada de herança múltipla em classes.
Variáveis e métodos privados podem ser declarados (por convenção, isso não é imposto pela linguagem)
adicionando pelo menos dois sublinhados iniciais e no máximo um final (por exemplo, __spam).
Também podemos vincular nomes arbitrários a instâncias de classe. Segue um exemplo:

.. code-block:: python

    class MinhaClasse(object):
        comum = 10
        def __init__(self):
            self.myvariable = 3
        def minhafunção(self, arg1, arg2):
            return self.myvariable

        # Esta é a instanciação da classe

    >>> instância_de_classe = MinhaClasse()
    >>> instância_de_classe.minhafunção(1, 2)
    3
    # Esta variável é compartilhada por todas as instâncias.
    >>> instância_de_classe2 = MinhaClasse()
    >>> instância_de_classe2.comum
    10
    >>> instância_de_classe22.comum
    10
    # Observe como usamos o nome da classe
    # em vez da instância.
    >>> MinhaClasse.comum = 30
    >>> instância_de_classe.comum
    30
    >>> instância_de_classe2.comum
    30
    # Isso não atualizará a variável na classe,
    # em vez disso, ele vinculará um novo objeto ao antigo
    # nome variável.
    >>> instância_de_classe.comum = 10
    >>> instância_de_classe.comum
    10
    >>> instância_de_classe2.comum
    30
    >>> MinhaClasse.comum = 50
    # Isso não mudou, porque "comum" é
    # agora uma variável de instância.
    >>> instância_de_classe.comum
    10
    >>> instância_de_classe2.comum
    50

    # Esta classe herda de MinhaClasse. O exemplo
    # classe acima herda de "object", o que torna
    # é o que chamamos de "classe de novo estilo".
    # Herança múltipla é declarada como:
    # class OtherClass(MinhaClasse1, MinhaClasse2, MinhaClasseN)
    class OutraClasse(MinhaClasse):
        # O argumento "self" é passado automaticamente
        # e se refere à instância da classe, então você pode definir
        # variáveis de instância como acima, mas de dentro da classe.
        def __init__(self, arg1):
            self.myvariable = 3
            print(arg1)

    >>> instância_de_classe = OutraClasse("Olá")
    Olá
    >>> instância_de_classe.minhafunção(1, 2)
    3
    # Esta classe não tem um membro .teste, mas
    # podemos adicionar um à instância de qualquer maneira. Observação
    # que este será apenas um membro da classinstance.
    >>> instância_de_classe.teste = 10
    >>> instância_de_classe.teste
    10

Exceções
--------

Exceções em Python são tratadas com blocos try-except [exceptionname]:

.. code-block:: python

    def alguma_função():
        try:
            # Divisão por zero gera uma exceção
            10/0
        except ZeroDivisionError:
            print("Opa, inválido.")
        else:
            # A exceção não ocorreu, estamos bem.
            pass
        finaly:
            # Isso é executado após o bloco de código ser executado
            # e todas as exceções foram tratadas, mesmo
            # se uma nova exceção for levantada durante o manuseio.
            print("Acabamos com isso.")

    >>> alguma_função()
    Ops, inválido.
    Acabamos com isso.

Importando
----------

Bibliotecas externas são usadas com a palavra-chave import [libname].
Você também pode usar from [libname] import [funcname] para funções individuais.
Aqui está um exemplo:

.. code-block:: python

    import random
    from time import clock

    randomint = random.randint(1, 100)
    >>> print(randomint)
    64

E/S de arquivo
--------------

O Python possui uma ampla variedade de bibliotecas incorporadas.
Como exemplo, aqui está como a serialização
(conversão de estruturas de dados em strings usando a biblioteca pickle)
com E/S de arquivo é usada:

.. code-block:: python

    import pickle
    minhalista = ["Isto", "é", 4, 13327]
    # Abra o arquivo C:\\binary.dat para escrita. A letra r antes do
    # string de nome de arquivo é usada para evitar o escape de barra invertida.
    meuarquivo = open(r"C:\\binary.dat", "wb")
    pickle.dump(minhalista, meuarquivo)
    meuarquivo.fechar()

    meuarquivo = open(r"C:\\text.txt", "w")
    meuarquivo.write("Esta é uma string de amostra")
    meuarquivo.close()

    meuarquivo = open(r"C:\\text.txt")
    >>> print(meuarquivo.read())
    'Esta é uma string de amostra'
    meuarquivo.close()

    # Abra o arquivo para leitura.
    meuarquivo = open(r"C:\\binary.dat", "rb")
    lista_carregada = pickle.load(meuarquivo)
    meuarquivo.fechar()
    >>> print(lista_carregada)
    ['Isto', 'é', 4, 13327]

    # Abra o arquivo para leitura usando with.
    with open(r"C:\\binary.dat", "rb") as meuarquivo:
        lista_carregada = pickle.load(meuarquivo)
        # não precisa fechar o arquivo, ao sair do bloco o with chama o close
        print(lista_carregada)
    ['Isto', 'é', 4, 13327]

Diversos
--------

    As condições podem ser encadeadas: 1 < a < 3 verifica se a é menor que 3 e maior que 1.
    Você pode usar del para excluir variáveis ou itens em arrays.
    As compreensões de lista fornecem uma maneira poderosa de criar e manipular listas.
    Eles consistem em uma expressão seguida por uma cláusula for seguida por zero ou mais cláusulas
    if ou for, assim:

.. code-block:: python

    >>> lst1 = [1, 2, 3]
    >>> lst2 = [3, 4, 5]
    >>> print([x * y for x in lst1 for y in lst2])
    [3, 4, 5, 6, 8, 10, 9, 12, 15]
    >>> print([x for x in lst1 if 4 > x > 1])
    [2, 3]
    # Verifica se uma condição é verdadeira para algum item.
    # "qualquer" retorna verdadeiro se algum item da lista for verdadeiro.
    >>> any([i % 3 para i em [3, 3, 4, 4, 3]])
    True
    # Isso ocorre porque 4 % 3 = 1, e 1 é verdadeiro, então any()
    # retorna True.

    # Verifica quantos itens uma condição é verdadeira.
    >>> sum(1 for i in [3, 3, 4, 4, 3] if i == 4)
    2
    >>> del lst1[0]
    >>> print(lst1)
    [2, 3]
    >>> del lst1

As variáveis globais são declaradas fora das funções e podem ser lidas
sem nenhuma declaração especial, mas se você quiser escrever nelas,
deve declará-las no início da função com a palavra-chave global, caso contrário,
o Python vinculará esse objeto a uma nova variável local (cuidado com isso,
é um pequeno problema que pode te pegar se você não souber). Por exemplo:

.. code-block:: python

    número = 5

    def minhafunc():
        # Isso imprimirá 5.
        print(número)

    def outra função():
        # Isso gera uma exceção porque a variável não
        # foi encadernado antes da impressão. Python sabe que é um
        # objeto será vinculado a ele mais tarde e cria um novo objeto local
        # em vez de acessar o global.
        print(número)
        número = 3

    def aindaoutrafunc():
        global número
        # Isso alterará corretamente o global.
        número = 3

Epílogo
-------

Este tutorial não pretende ser uma lista exaustiva de todos
(ou mesmo um subconjunto) do Python. Python tem uma vasta gama de bibliotecas
e muito mais funcionalidades que você terá que descobrir por outros meios,
como o excelente livro Dive into Python. Espero ter facilitado sua transição no Python.
Por favor, deixe comentários se você acredita que há algo que poderia ser melhorado
ou adicionado ou se há algo que você gostaria de ver (aulas, tratamento de erros, qualquer coisa).

.. note::
   Procure ser cooperativo com a sua equipe.
