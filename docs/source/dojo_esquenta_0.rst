.. include:: special.rst

.. _modulo_esquenta_zero:

Problemas para o Dojo de Aquecimento
====================================

1. Quando dormir
-------------------------

O parâmetro trabalho é True se for um dia de trabalho e o parâmetro férias é True se estivermos de férias.
Nós dormimos se não for um dia de trabalho ou estamos de férias. Retorne True se dormirmos até tarde..

.. raw:: html

  <div id="dojo_0"></div>
  <script type="text/python">
      from ScriptWidget import ScriptBuilder
      sw2 = ScriptBuilder("dojo_esquenta_0.py", height=200, title="dojo esquenta 0")
  </script>


2. Macacos encrenqueiros
--------------------------------------------------

Temos dois macacos, a e b, e os parâmetros a_sorri e b_sorri indicam se cada um está sorrindo.
Estamos em apuros se ambos estiverem sorrindo ou se nenhum deles estiver sorrindo.
Retorne True se estivermos com problemas..

.. raw:: html

  <div id="dojo_1"></div>

3. Soma ou dobro
---------------------------------

Dados dois valores int, retorne sua soma. Caso os dois valores sejam iguais, retorne o dobro da soma.

.. raw:: html

  <div id="dojo_2"></div>


4. Diferença para 21
------------------------------------------------------------------

Dado um int n, retorne a diferença absoluta entre n e 21,
exceto retorne o dobro da diferença absoluta se n for maior que 21..

.. raw:: html

  <div id="dojo_3"></div>

5. Papagaio Tagarela
---------------------------------

Temos um papagaio falando alto. O parâmetro "hora" é a hora atual no intervalo 0..23.
Estamos com problemas se o papagaio estiver falando e a hora for antes das 7 ou depois das 20.
Retorne True se estivermos com problemas..

.. raw:: html

  <div id="dojo_4"></div>

6. Dezena ou Soma
---------------------------------

Dados 2 inteiros, a e b, retorne True se um deles for 10 ou se sua soma for 10.

.. raw:: html

  <div id="dojo_5"></div>

7. Em torno de Cem
---------------------------------

Dado um int n, retorne True se estiver à distância menor que 10 do valor 100.
Nota: abs(num) calcula o valor absoluto de um número.

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
