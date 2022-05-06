.. include:: special.rst

.. _modulo_esquenta_um:

Problemas para o Dojo de Aquecimento 1
====================================

1. Multiplicando as palavras
-------------------------

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


2. Exclui letra
--------------------------------------------------

Dada uma string, retorne uma nova string feita de todos os outros caracteres começando com
o primeiro, então "Hello" produz "Hlo".

string_palavra('Hello') → 'Hlo'
string_palavra('Hi') → 'H'
string_palavra('Heeololeo') → 'Hello'



.. raw:: html

  <div id="dojo_1"></div>

3. Número Repetido
---------------------------------

Dado um array de ints, retorne a quantidade de números de 9 no array.

conta_numero([1, 2, 9]) → 1
conta_numero([1, 9, 9]) → 2
conta_numero([1, 9, 9, 3, 9]) → 3

.. raw:: html

  <div id="dojo_2"></div>


4. Sequência de Números
------------------------------------------------------------------

Dada uma matriz de ints, retorne True se a sequência de números 1, 2, 3 aparecer
na matriz em algum lugar.

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

