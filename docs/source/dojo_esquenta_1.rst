.. include:: special.rst

.. _modulo_esquenta_um:

Problemas para o Dojo de Aquecimento 1
======================================

1. Multiplicando as palavras
----------------------------

Dada uma string e um int n não negativo, diremos que a frente da string são os primeiros 3 caracteres,
ou o que estiver lá se a string for menor que 3. Retorna n cópias da frente;

frente_vezes('Chocolate', 2) → 'ChoCho'
frente_vezes('Chocolate', 3) → 'ChoChoCho'
frente_vezes('Abc', 3) → 'AbcAbcAbc'

.. raw:: html

  <div id="dojo_0"></div>
  <script type="text/python">
      from ScriptWidget import ScriptBuilder
      sw2 = ScriptBuilder("dojo_esquenta_1.py", height=200, title="dojo esquenta 0")
  </script>


2. Criando uma nova palavra
--------------------------------------------------

Dada uma string, retorne uma nova string feita de todos os outros caracteres começando com
o primeiro, então "Hello" produz "Hlo".



.. raw:: html

  <div id="dojo_1"></div>

3. Número Repetido
---------------------------------

Dado um array de ints, retorne a quantidade de números de 9 no array.

.. raw:: html

  <div id="dojo_2"></div>



Dada uma string, retorne a contagem do número de vezes que uma substring
de comprimento 2 aparece na string e também como os últimos 2 caracteres da
string, então "hixxxhi" produz 1 (não contaremos a substring final).


4. É ou não é
------------------------------------------------------------------
Dado um array de ints, retorne True se um dos primeiros 4 elementos do array for 9.
O comprimento do array pode ser menor que 4.


.. raw:: html

  <div id="dojo_3"></div>

5. Sequência de Números
---------------------------------

Dada uma matriz de ints, retorne True se a sequência de números 1, 2, 3 aparecer
na matriz em algum lugar.

.. raw:: html

  <div id="dojo_4"></div>

6. Explosão de Letras
---------------------------------

Dada uma string não vazia como "Code", retorne uma string como "CCoCodCode".

.. raw:: html

  <div id="dojo_5"></div>

7. Posições Iguais
---------------------------------

Dadas 2 strings, a e b, retorne o número de posições onde elas contêm a mesma substring de comprimento 2.
Portanto, "xxcaazz" e "xxbaaz" resultam em 3, já que as substrings "xx", "aa" e "az" aparecem no mesmo
lugar em ambas as strings.
.. raw:: html

  <div id="dojo_6"></div>

8. Negatividade
---------------------------------

Dados 2 valores int, retorne True se um for negativo e um for positivo.
Exceto se o parâmetro "negativo" for True, então retorne True somente se ambos forem negativos.

.. raw:: html

  <div id="dojo_7"></div>

9. Negação
---------------------------------

Dada uma string, retorne uma nova string onde "nega " foi adicionado à frente.
No entanto, se a string já começar com "nega", retorne a string inalterada..

.. raw:: html

  <div id="dojo_8"></div>

10. Eliminação
---------------------------------

Dada uma string não vazia e um int n, retorne uma nova string onde o char no índice n foi removido.
O valor de n será um índice válido de um char na string original
(ou seja, n estará no intervalo 0..len(str)-1 inclusive).

.. raw:: html

  <div id="dojo_9"></div>

11. Trocação
---------------------------------

Dada uma string, retorne uma nova string onde o primeiro e a última letras foram trocadas.

.. raw:: html

  <div id="dojo_a"></div>

12. Copiação
---------------------------------

Dada uma string, diremos que a frente são os 3 primeiros caracteres da string.
Se o comprimento da string for menor que 3, a frente é o que estiver lá.
Retorna uma nova string que tem 3 cópias da frente..

.. raw:: html

  <div id="dojo_b"></div>

