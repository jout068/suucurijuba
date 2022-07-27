#! /usr/bin/env python
# -*- coding: UTF8 -*-
# This file is part of  program Intro Python
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

"""*Dojo* Esquenta -

    Desafios muito simples.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    22.05
        Criação dos desafios.


.. seealso::

   Página Original na internete: CodingBat_

.. _CodingBat: https://codingbat.com/python/Warmup-2
"""
_SET0_ = {
    "script_name": "dojo_0", "script_div_id": "dojo_0",
    "height": 200, "title": "Tijolos"
}  # _SEC_
def fazer_tijolos(pequeno, grande, objetivo):
    """Retornar True se for possivel fazer a fileira de tijolos.
    """


_SET1_ = {
    "script_name": "dojo_1",    "script_div_id": "dojo_1",
    "height": 200, "title": "Soma dos valores"
}  # _SEC_

def soma_valores(a,b,c):
    """Retorne a soma dos valores, mas se um dos valores for igual
    a outro dos valores, ele não conta para a soma.
    """


assert soma_valores(1,2,3) == 6
assert soma_valores(3,2,3) == 2
assert soma_valores(3,3,3) == 0

_SET2_ = {
    "script_name": "dojo_2",    "script_div_id": "dojo_2",
    "height": 200, "title": "numero repetido"
}  # _SEC_
def numero_sorte(numero):
    """Retorna a soma de 3 valores, mas se um dos valores for 13, ele
    não conta para a soma e os valores da direita não contam também.
    """


assert numero_sorte(1,2,3) == 6
assert numero_sorte(1,2,13) == 3
assert numero_sorte(1,13,3) == 1

_SET3_ = {
    "script_name": "dojo_3",    "script_div_id": "dojo_3",
    "height": 200, "title": "Quilos de chocolate"
}  # _SEC_
def quilo_chocolate(matriz):
    """Retorna o número de barras pequenas a serem usadas.
    """



assert quilo_chocolate(4,1,9) == 4
assert quilo_chocolate(4,1,10) == -1
assert quilo_chocolate(4,1,7) == 2
_SET4_ = {
    "script_name": "dojo_4",    "script_div_id": "dojo_4",
    "height": 200, "title": "Letras repetidas"
}  # _SEC_
def letras_repetidas(palavra):
    """Retornar a palavra com todas as letras repetidas
    """



assert letras_repetidas('The') == 'TThhee'
assert letras_repetidas('AAbb') == 'AAAAbbbb'
assert letras_repetidas('Ola Ara') == 'OOllaa AArraa'

_SET5_ = {
    "script_name": "dojo_5",    "script_div_id": "dojo_5",
    "height": 200, "title": "Contando String"
}  # _SEC_
def contando_string(palavra):
    ""


assert contando_string('Code') == ('CCoCodCode')
assert contando_string('abc') == ('aababc')
assert contando_string('ab') == ('aab')

_SET6_ = {
    "script_name": "dojo_6",    "script_div_id": "dojo_6",
    "height": 200, "title": "Gato e Cachorros"
}  # _SEC_
def gato_cachorro(palavra):
  """Retorna True se aparecer 'gato' e 'cachorro' na string fornecida
  """




assert gato_cachorro('gatocachorro') == True
assert gato_cachorro('gatogato') == False
assert gato_cachorro('1gato1gacacachorro') == True
_SET7_ = {
    "script_name": "dojo_7",    "script_div_id": "dojo_7",
    "height": 200, "title": "Final da palavra"
}  # _SEC_
def palavra_final(a,b):
    """Retorna se apenas um é negativo ou se os dois são.
    """


assert palavra_final('Hiabc','abc') == True
assert palavra_final('AbC', 'HiaBc') == True
assert palavra_final('abc', 'abXabc') == True

_SET8_ = {
    "script_name": "dojo_8",    "script_div_id": "dojo_8",
    "height": 200, "title": "Numeros inteiros"
}  # _SEC_
def matriz_inteiros(matriz):
    """ 'Retorna o número de inteiros pares na matriz fornecida.
    """


assert matriz_inteiros([2,1,2,3,4]) == 3
assert matriz_inteiros(2,2,0) == 3
assert matriz_inteiros(1,3,5) == 0

_SET9_ = {
    "script_name": "dojo_9",    "script_div_id": "dojo_9",
    "height": 200, "title": "Diferença maior e menor"
}  # _SEC_
def maior_menor(numeros):
    """ Retorna a diferença entre o maior e o menor
    valor na matriz.
    """



assert maior_menor([10,3,5,6]) == 7
assert maior_menor([7,2,10,9]) == 8
assert maior_menor([2,10,7,2]) == 8

_SETA_10 = {
    "script_name": "dojo_10",    "script_div_id": "dojo_10",
    "height": 200, "title": "Soma das matrizes"
}  # _SEC_
def soma_matriz(texto):
    """ Retorna a soma dos números na matriz.
    """



assert soma_matriz([1,2,2,1]) == 6
assert soma_matriz([1,1]) == 2
assert soma_matriz([1,2,2,1,13]) == 6

_SET11_ = {
    "script_name": "dojo_11",    "script_div_id": "dojo_11",
    "height": 200, "title": "Tem Dois 2"
}  # _SEC_
def tem22(texto):
    """ Retorna TRue se a matriz tiver um 2 próximo
     a um 2 em algum lugar.
    """



assert tem22([1,2,2]) == True
assert tem22([1,2,1,2]) == False
assert tem22([2,1,2]) == False

_SET12_ = {
    "script_name": "dojo_12", "script_div_id": "dojo_12",
    "height": 200, "title": "Tijolos"
}  # _SEC_
def fazer_tijolos(pequeno, grande, objetivo):
    """Retornar True se for possivel fazer a fileira de tijolos.
    """


_SET13_ = {
    "script_name": "dojo_13",    "script_div_id": "dojo_13",
    "height": 200, "title": "Soma dos valores"
}  # _SEC_

def soma_valores(a,b,c):
    """Retorne a soma dos valores, mas se um dos valores for igual
    a outro dos valores, ele não conta para a soma.
    """


assert soma_valores(1,2,3) == 6
assert soma_valores(3,2,3) == 2
assert soma_valores(3,3,3) == 0

_SET14_ = {
    "script_name": "dojo_14",    "script_div_id": "dojo_14",
    "height": 200, "title": "numero repetido"
}  # _SEC_
def numero_sorte(numero):
    """Retorna a soma de 3 valores, mas se um dos valores for 13, ele
    não conta para a soma e os valores da direita não contam também.
    """


assert numero_sorte(1,2,3) == 6
assert numero_sorte(1,2,13) == 3
assert numero_sorte(1,13,3) == 1

_SET15_ = {
    "script_name": "dojo_15",    "script_div_id": "dojo_15",
    "height": 200, "title": "Quilos de chocolate"
}  # _SEC_
def quilo_chocolate(matriz):
    """Retorna o número de barras pequenas a serem usadas.
    """



assert quilo_chocolate(4,1,9) == 4
assert quilo_chocolate(4,1,10) == -1
assert quilo_chocolate(4,1,7) == 2
_SET16_ = {
    "script_name": "dojo_16",    "script_div_id": "dojo_16",
    "height": 200, "title": "Letras repetidas"
}  # _SEC_
def letras_repetidas(palavra):
    """Retornar a palavra com todas as letras repetidas
    """



assert letras_repetidas('The') == 'TThhee'
assert letras_repetidas('AAbb') == 'AAAAbbbb'
assert letras_repetidas('Ola Ara') == 'OOllaa AArraa'

_SET17_ = {
    "script_name": "dojo_17",    "script_div_id": "dojo_17",
    "height": 200, "title": "Contando String"
}  # _SEC_
def contando_string(palavra):
    ""


assert contando_string('Code') == ('CCoCodCode')
assert contando_string('abc') == ('aababc')
assert contando_string('ab') == ('aab')

_SET18_ = {
    "script_name": "dojo_18",    "script_div_id": "dojo_18",
    "height": 200, "title": "Gato e Cachorros"
}  # _SEC_
def gato_cachorro(palavra):
  """Retorna True se aparecer 'gato' e 'cachorro' na string fornecida
  """




assert gato_cachorro('gatocachorro') == True
assert gato_cachorro('gatogato') == False
assert gato_cachorro('1gato1gacacachorro') == True
_SET19_ = {
    "script_name": "dojo_19",    "script_div_id": "dojo_19",
    "height": 200, "title": "Final da palavra"
}  # _SEC_
def palavra_final(a,b):
    """Retorna se apenas um é negativo ou se os dois são.
    """


assert palavra_final('Hiabc','abc') == True
assert palavra_final('AbC', 'HiaBc') == True
assert palavra_final('abc', 'abXabc') == True

_SET20_ = {
    "script_name": "dojo_20",    "script_div_id": "dojo_20",
    "height": 200, "title": "Numeros inteiros"
}  # _SEC_
def matriz_inteiros(matriz):
    """ 'Retorna o número de inteiros pares na matriz fornecida.
    """


assert matriz_inteiros([2,1,2,3,4]) == 3
assert matriz_inteiros(2,2,0) == 3
assert matriz_inteiros(1,3,5) == 0

_SET9_ = {
    "script_name": "dojo_9",    "script_div_id": "dojo_9",
    "height": 200, "title": "Diferença maior e menor"
}  # _SEC_
def maior_menor(numeros):
    """ Retorna a diferença entre o maior e o menor
    valor na matriz.
    """



assert maior_menor([10,3,5,6]) == 7
assert maior_menor([7,2,10,9]) == 8
assert maior_menor([2,10,7,2]) == 8

_SETA_ = {
    "script_name": "dojo_a",    "script_div_id": "dojo_a",
    "height": 200, "title": "Soma das matrizes"
}  # _SEC_
def soma_matriz(texto):
    """ Retorna a soma dos números na matriz.
    """



assert soma_matriz([1,2,2,1]) == 6
assert soma_matriz([1,1]) == 2
assert soma_matriz([1,2,2,1,13]) == 6

_SETB_ = {
    "script_name": "dojo_b",    "script_div_id": "dojo_b",
    "height": 200, "title": "Tem Dois 2"
}  # _SEC_
def tem22(texto):
    """ Retorna TRue se a matriz tiver um 2 próximo
     a um 2 em algum lugar.
    """



assert tem22([1,2,2]) == True
assert tem22([1,2,1,2]) == False
assert tem22([2,1,2]) == False
