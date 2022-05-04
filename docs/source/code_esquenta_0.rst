..  # This file is part of  program Intro Python
    # Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
    # `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
    # SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

    Programação Esquenta Zero

        Operações condicionais.

    Changelog
    22.04
            Criação do tutorial.
    22.04.25
            Adicionou Numéricos.

.. include:: special.rst

.. _modulo_code_esquenta_zero:

Aprendendo Operações
====================================

1. Tipo Booleano
-------------------------

A lógica booleana é uma forma de matemática onde existem apenas dois valores **Verdadeiro** (:red:`True`)
e **Falso** (:red:`False`)

.. raw:: html

  <div id="code_0"></div>
  <script type="text/python">
      from ScriptWidget import ScriptBuilder
      sw2 = ScriptBuilder("code_esquenta_0.py", height=200, title="dojo esquenta 0")
  </script>

2. Comparações Lógicas
-------------------------

Uma forma de controlar o que o seu programa faz é o uso de operações condicionais.
O comando :red:`if` *<comparação>* :red:`:` *<faz se verdadeiro>*  :red:`else:` *<faz se falso>*

.. raw:: html

  <div id="code_1"></div>

3. Conectores Lógicos
-------------------------

As linguagens de programação, utilizam os conectivos lógicos da lógica formal, ou melhor da lógica Aristotélica,
na construção de expressões lógicas. Existem 2 conectivos lógicos e,
mesmo que não os conheçamos com o nome de conectivos lógicos, utilizamo-os constantemente ao conversarmos ou então,
para explicarmos qualquer disciplina a outra pessoa.

Os conectivos lógicos são:

        :Conectivo de conjunção: E :red:`and`
        :Conectivo de disjunção: OU :red:`or`
        :Partícula de Negação: NÃO :red:`not`

Por exemplo, a simples frase A e B são caracteres iguais implica numa expressão lógica e acabamos de representar
a mesma textualmente. Porém, a expressão pode ser facilmente escrita matematicamente, ou então,
com o uso de uma linguagem de programação.

.. raw:: html

  <div id="code_2"></div>

4. Comparações Numéricas
-------------------------

Você pode comparar dois números em Python como se faz na matemática.

Os comparadores numéricos são:

        :Menor: :red:`<`
        :Menor ou Igual: :red:`<=`
        :Igual: :red:`==`
        :Maior: :red:`>`
        :Maior ou Igual: :red:`>=`
        :Diferente: :red:`!=`

.. raw:: html

  <div id="code_3"></div>

4. Expressões Numéricas
-------------------------

Você pode comparar três números em Python como se faz na matemática.

Os comparadores numéricos são aqueles já explicados:

.. raw:: html

  <div id="code_4"></div>

.. note::

   Agora você pode tentar os desafios de 1 a 8 do : :ref:`modulo_esquenta_zero`

.. seealso::

   Página de Referência na internete: `OPERADORES LÓGICOS EM PYTHON`_

.. _`OPERADORES LÓGICOS EM PYTHON`: http://excript.com/python/operadores-logicos-python.html
