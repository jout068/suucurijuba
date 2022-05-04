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
.. versionadded::    22.04
        Criação dos desafios.


.. seealso::

   Página Original na internete: CodingBat_

.. _CodingBat: https://codingbat.com/python/Warmup-1
"""
_SET0_ = {
    "script_name": "dojo_0", "script_div_id": "dojo_0",
    "height": 200, "title": "dormir até tarde"
}  # _SEC_
def dormir_ate_tarde(trabalho, ferias):
    """Decide quando dormir até tarde.
    """
    _ = trabalho, ferias
    dormir = False
    return dormir


assert dormir_ate_tarde(True, True) is True

_SET1_ = {
    "script_name": "dojo_1",    "script_div_id": "dojo_1",
    "height": 200, "title": "Macacos encrenqueiros"
}  # _SEC_
def macacos_encrenqueiros(a_sorri, b_sorri):
    """Observe os macacos e veja se é encrenca.
    """
    _ = a_sorri, b_sorri
    encrenca = 0x0
    return encrenca


assert macacos_encrenqueiros(True, True) is True
assert macacos_encrenqueiros(False, False) is True
assert macacos_encrenqueiros(False, True) is False

_SET2_ = {
    "script_name": "dojo_2",    "script_div_id": "dojo_2",
    "height": 200, "title": "Soma ou dobro"
}  # _SEC_
def soma_ou_dobro(um_numero, outro_numero):
    """Calcule a soma ou o dobro da soma.
    """
    _ = um_numero, outro_numero
    soma_dobro = 0
    return soma_dobro


assert soma_ou_dobro(2, 3) == 5
assert soma_ou_dobro(2, 2) == 8

_SET3_ = {
    "script_name": "dojo_3",    "script_div_id": "dojo_3",
    "height": 200, "title": "Diferença para 21"
}  # _SEC_
def diferenca21(um_numero):
    """Retorne a diferença para 21 ou o dobro.
    """
    _ = um_numero
    return um_numero


assert diferenca21(19) == 2
assert diferenca21(23) == 4

_SET4_ = {
    "script_name": "dojo_4",    "script_div_id": "dojo_4",
    "height": 200, "title": "Papagaio Tagarela"
}  # _SEC_
def papagaio_tagarela(falando, hora):
    """Retorna se Papagaio Tagarela cria encrenca.
    """
    _ = falando, hora
    encrenca = True
    return encrenca


assert papagaio_tagarela(True, 9) is False
assert papagaio_tagarela(False, 21) is False
assert papagaio_tagarela(True, 6) is True

_SET5_ = {
    "script_name": "dojo_5",    "script_div_id": "dojo_5",
    "height": 200, "title": "Dezena ou Soma"
}  # _SEC_
def dezena_soma(um_numero, outro_numero):
    """Retorna se um deles é uma dezena ou a soma é.
    """
    resultado = um_numero, outro_numero
    return resultado


assert dezena_soma(10, 4) is True
assert dezena_soma(3, 7) is True
assert dezena_soma(2, 4) is False

_SET6_ = {
    "script_name": "dojo_6",    "script_div_id": "dojo_6",
    "height": 200, "title": "Em torno de Cem"
}  # _SEC_
def aproximadamente_cem(valor):
    """Retorna se o número está nas proximidades do número cem.
    """
    resultado = valor
    return resultado


assert aproximadamente_cem(109) is True
assert aproximadamente_cem(92) is True
assert aproximadamente_cem(89) is False

_SET7_ = {
    "script_name": "dojo_7",    "script_div_id": "dojo_7",
    "height": 200, "title": "Negatividade"
}  # _SEC_
def negatividade(um_numero, outro_numero, negativo):
    """Retorna se apenas um é negativo ou se os dois são.
    """
    resultado = um_numero, outro_numero, negativo
    return resultado


assert negatividade(-2, -2, False) is False
assert negatividade(-2, -2, True) is True
assert negatividade(-2, 3, False) is True

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
