.. _modulo_dez_zero:

.. include:: special.rst

Funcionalidades Primárias
=========================

Vamos nos concentrar no Python 3, em especial no `Brython`_
que é uma versão que executa dentro do navegador.

Python como uma calculadora
---------------------------
Python é como se fosse uma calculadora mais avançada. Voce pode operar
dois números usando “:red:`+`”, “:red:`-`”, “:red:`/`” ou “:red:`*`” ( multiplicação).

.. raw:: html

  <div id="dojo_pre_0"></div>
  <script type="text/python">
      from ScriptWidget import ScriptBuilder
      sw2 = ScriptBuilder("dojo_pre.py", height=100, index="0.0", title="dojo preliminar")
  </script>


Usando a Memória
-----------------

Em uma calculdora comum você pode salvar um número na memória e depois recuperar.
No Python, você pode usar qualquer nome para designar a memória. Você usa “:red:`=`”
para guardar algo num nome que fica antes do igual. Depois usa o nome para recuperar
o valor apontado.

.. raw:: html

  <div id="dojo_pre_1"></div>

Memória Como Uma Lista
----------------------

Você também pode usar uma memória maior criando uma lista de valores.
Você pode criar uma lista implícita usando :red:`[`  e :red:`]`.
Também pode ter um objeto lista criando com :red:`list()`.
Você pode usar no parâmetro uma lista implícita ou um objeto intervalo.
O  objeto intervalo é criado com :red:`range()`.
Se tiver só um parâmetro, significa intervalo de zero até aquele número, exclusive :red:`range(fim)`.
Se tiver dois é o início e o fim do intervalo :red:`range(inicio, fim)`
Se tiver três, o último diz a razão de quanto pula na sequência :red:`range(inicio, fim, pulo)`

.. raw:: html

  <div id="dojo_pre_2"></div>

Usando listas
--------------

As lista podem ser percorridas para se aproveitar cada item da lista.
Uma maneira é usando o comando  :red:`for`.
No :red:`for` voce usa um intervalo ou uma lista e nomeia o item da vez:

:red:`for` item_da_vez :red:`in` nome_da_lista_ou_intervalo :red:`:`
    <faz alguma coisa aqui>

Você também pode criar uma lista dinamicamente da forma implícita:

:red:`[` item_da_vez :red:`for` item_da_vez :red:`in` nome_da_lista_ou_intervalo :red:`]`

.. raw:: html

  <div id="dojo_pre_3"></div>

Propriedades das Listas
-----------------------

Cada item de uma lista pode ser acessado pelo índice de sua posição nela.
Os itens guardados em uma lista podem ser acessados usando  :red:`[]`.
O número colocado entre chaves é a posição na lista começando por zero.
Nos exemplos abaixo temos outras facilidades de acesso a uma lista.

.. raw:: html

  <div id="dojo_pre_3_1"></div>

Usando o Navegador para Criar Conteúdo
--------------------------------------
Brython_ quer dizer Browser-Python, ou seja, um Python que interage como o navegador.
No **Brython** você tem objetos especiais para acessar e modificar coisas no navegador.
No navegador, partes podem ser identificadas por um nome e o Brython usa este nome
para interagir com esta parte. O pacote **browser** pode ser importado para uso com:

:red:`from`  browser :red:`import` document

Por exemplo, bem aqui embaixo está uma parte que tem
o nome **um_texto**. No código vamos identificar esta parte e escrever um texo ali.

.. raw:: html

  <div id="um_texto"></div></br>
  <div id="dojo_pre_4"></div>

Desenhando com o Brython
------------------------

Podemos desenhar no navegador usando um padrão SVG_ (Scalable Vector Graphics).
O pacote **browser** contem tambem o objeto svg que pode ser importado para uso com:

:red:`from`  browser :red:`import` svg

O comando svg do pacote svg (:red:`svg.svg`) cria uma tela onde você pode desenhar usando este padrão.
O operador :red:`<=` significa adicionar algo na tela ou mesmo adicionar um objeto dentro de outro.
Vamos desenhar coisas dentro de uma parte que está bem aqui em baixo chamada **um_desenho**.
Tente desenhar um boneco de palitos usando alguns dos comandos apresentados.

.. raw:: html

  <div id="um_desenho" style="min-height:200px;"></div></br>
  <div id="dojo_pre_5"></div>


Desafio do Arco Iris
--------------------------------
Use um comando for para desenhar as cores do arco iris com retângulos.
Use a parte abaixo chamada **arco_iris**. Veja a imagem exemplo abaixo.
Um desafio maior seria desenhar o arco-iris usando o comando svg.path 🌈.

.. image:: _static/iris.png

.. raw:: html

  <div id="arco_iris" style="min-height:200px;"></div></br>
  <div id="dojo_pre_6"></div>


Desafio do Quadro de Bandeirinhas
---------------------------------
`Alfredo Volpi`_ foi um artista brasileiro que gostava de pintar bandeirinhas.
Use um comando for para desenhar bandeirinhas de várias cores.
Use a parte abaixo chamada **volpi**. Veja a imagem exemplo abaixo.
Você pode usar o comando :red:`choice` do pacote :red:`random` para sortear uma cor
diferente para cada bandeirinha.

.. image:: _static/volpi.png

.. raw:: html

  <div id="volpi" style="min-height:200px;"></div></br>
  <div id="dojo_pre_7"></div>


.. note::
   Você também pode tentar resolver algo no dojo inicial: :ref:`modulo_dojo_zero`

.. _Brython: https://www.brython.info
.. _SVG: https://www.devmedia.com.br/introducao-ao-svg-scalable-vector-graphics/27280
.. _Alfredo Volpi: https://www.wikiart.org/pt/alfredo-volpi/