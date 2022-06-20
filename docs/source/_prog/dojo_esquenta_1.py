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
    "height": 200, "title": "multiplicar o inicio"
}  # _SEC_
def multiplicar_o_inicio(inicio, n):
    """Multiplica os três primeiros caracteres.
    """
    inicio_len = 3
    if inicio_len > len(inicio):
        inicio_len = len(inicio)
    palavraFinal = inicio[:inicio_len]
    resultado = ""
    for i in range(n):
        resultado = resultado + palavraFinal
    return resultado

assert multiplicar_o_inicio('Chocolate', 2) == ('ChoCho')
assert multiplicar_o_inicio('Chocolate', 3) == ('ChoChoCho')


_SET1_ = {
    "script_name": "dojo_1",    "script_div_id": "dojo_1",
    "height": 200, "title": "criando uma nova palavra"
}  # _SEC_

def exclui_letra(palavra):
    """Exclui caracter sim e outro não.
    """
    resultado = ""
    for i in range(len(palavra)):
        if i % 2 == 0:
            resultado = resultado + palavra[i]

    return resultado


assert exclui_letra("Hello") == ('Hlo')
assert exclui_letra('Heeololeo') == ("Hello")

_SET2_ = {
    "script_name": "dojo_2",    "script_div_id": "dojo_2",
    "height": 200, "title": "numero repetido"
}  # _SEC_
def numero_repetido(numero):
    """Verifica se há o número 9 nos quatro primeiro elemento do array.
    """
    # conta = 0
    # for num in numero:
    #     if num == 9:
    #         conta = conta + 1
    # return conta


assert numero_repetido([1, 9, 9, 3, 9]) == 3
assert numero_repetido([1, 9, 9]) == 2

_SET3_ = {
    "script_name": "dojo_3",    "script_div_id": "dojo_3",
    "height": 200, "title": "É ou não é"
}  # _SEC_
def verifica_nove(matriz):
    """Retorna True se um dos quatros primeiros numeros da matriz for nove
    """
    fim = len(matriz)
    if fim > 4:
        fim = 4

        for i in range(fim):
            if matriz[i] == 9:
                return True
        return False

assert verifica_nove([1, 2, 9, 3, 4]) == True
assert verifica_nove([1, 2, 3, 4, 9]) == False

_SET4_ = {
    "script_name": "dojo_4",    "script_div_id": "dojo_4",
    "height": 200, "title": "Sequencia de numero"
}  # _SEC_
def sequencia_numero(matriz):
    """Retorne True caso a sequência de números 1, 2, 3 aparecer na matriz
    """
    for i in range(len(matriz) - 2):
        if matriz[i] == 1 and matriz[i + 1] == 2 and matriz[i + 2] == 3:
            return True
    return False


assert sequencia_numero([1, 1, 2, 3, 1]) == True
assert sequencia_numero([1, 1, 2, 4, 1]) == False

_SET5_ = {
    "script_name": "dojo_5",    "script_div_id": "dojo_5",
    "height": 200, "title": "Explosão de letras"
}  # _SEC_
def explosao_letras(palavra):

  palavraFinal = ""

  for i in range(len(palavra)):
    palavraFinal = palavraFinal + palavra[:i+1]
  return palavraFinal


assert explosao_letras('Code') == ('CCoCodCode')
assert explosao_letras('abc') == ('aababc')
assert explosao_letras('ab') == ('aab')

_SET6_ = {
    "script_name": "dojo_6",    "script_div_id": "dojo_6",
    "height": 200, "title": "Posições Iguais"
}  # _SEC_
def verifica_posicao(palavra1, palavra2):
    posicaoIgual = 0

    for i in range(len(palavra1) - 1):
        if palavra1[i:i + 2] == palavra2[i:i + 2]:
            posicaoIgual = posicaoIgual + 1
    return posicaoIgual


assert verifica_posicao('xxcaazz', 'xxbaaz') == 3
assert verifica_posicao('abc', 'abc') == 2
assert verifica_posicao('abc', 'axc') == 0
_SET7_ = {
    "script_name": "dojo_7",    "script_div_id": "dojo_7",
    "height": 200, "title": "Posições Iguais"
}  # _SEC_
def posicao_igual(um_numero, outro_numero, negativo):
    """Retorna se apenas um é negativo ou se os dois são.
    """
    resultado = um_numero, outro_numero, negativo
    return resultado



_SET8_ = {
    "script_name": "dojo_8",    "script_div_id": "dojo_8",
    "height": 200, "title": "Negação"
}  # _SEC_
def negacao(texto):
    """ 'Nega'uma string a não ser que já veio negada.
    """
    resultado = texto
    return resultado


assert negacao("agora") == "nega agora"
assert negacao("nega mais tarde") == "nega mais tarde"

_SET9_ = {
    "script_name": "dojo_9",    "script_div_id": "dojo_9",
    "height": 200, "title": "Eliminação"
}  # _SEC_
def eliminacao(texto, posicao):
    """ 'Elimina a letra na posição dada.
    """
    resultado = texto, posicao
    return resultado


assert eliminacao("agora",1) == "aora"
assert eliminacao("tarde", 0) == "arde"

_SETA_ = {
    "script_name": "dojo_a",    "script_div_id": "dojo_a",
    "height": 200, "title": "Trocação"
}  # _SEC_
def trocacao(texto):
    """ Troca a primeira letra pela última.
    """
    resultado = texto
    return resultado


assert trocacao("nunca") == "auncn"
assert trocacao("nega mais tarde") == "eega mais tardn"

_SETB_ = {
    "script_name": "dojo_b",    "script_div_id": "dojo_b",
    "height": 200, "title": "Copiação"
}  # _SEC_
def copiacao(texto):
    """ Copia as primeiras letras três vezes.
    """
    resultado = texto
    return resultado


assert copiacao("agora") == "agoagoago"
assert copiacao("um") == "umumum"
