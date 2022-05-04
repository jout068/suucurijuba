.. include:: special.rst

.. _modulo_dojo_zero:

Problemas para o Dojo Inicial
===============================

1. Ordene uma lista
-------------------------

Crie uma função em Python que aceite dois parâmetros.
O primeiro será uma lista de números. O segundo parâmetro será uma string que pode ter
um dos seguintes valores: asc, desc e none.
Se o segundo parâmetro for "asc", a função deve retornar uma lista com os números em ordem crescente.
Se for "desc", a lista deve estar em ordem decrescente e, se for "none",
deve retornar a lista original inalterada.

.. raw:: html

  <div id="dojo_0"></div>
  <script type="text/python">
      from ScriptWidget import ScriptBuilder
      sw2 = ScriptBuilder("dojo_basico_0.py", height=400, index="1.1", title="dojo básico")
  </script>


2. Converta um número decimal em binário
--------------------------------------------------

Escreva uma função em Python que aceite um número decimal e retorne o número binário equivalente.
Para simplificar, o número decimal sempre será menor que 1.024, portanto,
o número binário retornado sempre terá menos de dez dígitos.

.. raw:: html

  <div id="dojo_1"></div>

3. Conte as vogais em uma string
---------------------------------

Crie uma função em Python que aceite uma única palavra e retorne o número de vogais dessa palavra.
Nesta função, apenas a, e, i, o e u serão contados como vogais — não y.

.. raw:: html

  <div id="dojo_2"></div>


4. Oculte o número do cartão de crédito
------------------------------------------------------------------

Escreva uma função em Python que aceite um número de cartão de crédito.
Ele deve retornar uma string onde todos os caracteres estão ocultos com um asterisco,
exceto os quatro últimos. Por exemplo, se a função for enviada "4444444444444444",
ela deverá retornar "############4444".

.. raw:: html

  <div id="dojo_3"></div>

5. Os Xs são iguais aos Os?
---------------------------------

Crie uma função Python que aceite uma string. Esta função deve contar
o número de Xs e o número de Os na string. Ele deve retornar um valor booleano de True ou False.
Se a contagem de Xs e Os for igual, a função deve retornar True.
Se a contagem não for a mesma, deve retornar False.
Se não houver Xs ou Os na string, ela também deve retornar True porque 0 é igual a 0.
A string pode conter qualquer tipo e número de caracteres.

.. raw:: html

  <div id="dojo_4"></div>

6. Crie uma função de calculadora
---------------------------------

Escreva uma função Python que aceite três parâmetros. O primeiro parâmetro é um número inteiro.
O segundo é um dos seguintes operadores matemáticos: +, -, / ou .
O terceiro parâmetro também será um número inteiro.
A função deve realizar um cálculo e retornar os resultados.
Por exemplo, se a função for passada 6 e 4, ela deve retornar 24.

.. raw:: html

  <div id="dojo_5"></div>

7. Dê-me o desconto
---------------------------------

Crie uma função em Python que aceite dois parâmetros.
O primeiro deve ser o preço total de um item como um número inteiro.
O segundo deve ser a porcentagem de desconto como um número inteiro.

A função deve retornar o preço do item após a aplicação do desconto.
Por exemplo, se o preço for 100 e o desconto for 20, a função deve retornar 80.

.. raw:: html

  <div id="dojo_6"></div>

8. Apenas os números
---------------------------------

Escreva uma função em Python que aceite uma lista de qualquer tamanho
que contenha uma mistura de inteiros não negativos e strings.
A função deve retornar uma lista apenas com os inteiros da lista original na mesma ordem.

.. raw:: html

  <div id="dojo_7"></div>

9. Repita os caracteres
---------------------------------

Crie uma função Python que aceite uma string.
A função deve retornar uma string, com cada caractere na string original duplicado.
Se você enviar a função "agora" como parâmetro, ela deve retornar "aaggoorraa",
e se você enviar "123a!", ela deve retornar "112233aa!!".

.. raw:: html

  <div id="dojo_8"></div>
