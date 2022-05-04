#! /usr/bin/env python
# -*- coding: UTF8 -*-
# This file is part of  program Intro Python
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

"""Programação Esquenta Zero-

    Operações condicionais.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    22.04
        Criação do tutorial.


.. seealso::

   Página Original na internete: `OPERADORES LÓGICOS EM PYTHON`_

.. _`OPERADORES LÓGICOS EM PYTHON`: http://excript.com/python/operadores-logicos-python.html
"""
_SET0_ = {
    "script_name": "code_0", "script_div_id": "code_0",
    "height": 150, "title": "Tipo booleano"
}  # _SEC_
print(type(True))
print(type(False))
print(type(1 == 1))

_SET1_ = {
    "script_name": "code_1",    "script_div_id": "code_1",
    "height": 150, "title": "Operação condicional"
}  # _SEC_
if 1 == 1:
    print("um igual a um")

if 1 != 1:
    print("um difere de um")
else:
    print("um não difere de um")

_SET2_ = {
    "script_name": "code_2",    "script_div_id": "code_2",
    "height": 150, "title": "Conectores Lógicos"
}  # _SEC_
verdade = True
mentira = False
print('verdade or mentira :', verdade or mentira)
print('verdade and mentira :', verdade and mentira)
print('verdade and not mentira :', verdade and not mentira)
print('not verdade or mentira :', not verdade or mentira)

_SET3_ = {
    "script_name": "code_3",    "script_div_id": "code_3",
    "height": 190, "title": "Comparadores Numéricos"
}  # _SEC_
pequeno = 1
medio = 2
grande = 3
print('pequeno < grande :', pequeno < grande)
print('grande > medio :', grande > medio)
print('grande != pequeno :', grande != pequeno)
print('pequeno == grande :', pequeno == grande)
print('pequeno >= pequeno :', pequeno >= pequeno)
print('grande <= grande :', grande <= grande)

_SET4_ = {
    "script_name": "code_4",    "script_div_id": "code_4",
    "height": 190, "title": "Expressões Comparadoras"
}  # _SEC_
pequeno = 1
medio = 2
grande = 3
enorme = 9
print('pequeno < medio < grande :', pequeno < medio < grande)
print('grande > medio > pequeno :', grande > medio > pequeno)
print('grande > medio < enorme) :', grande > medio < enorme)
print('grande > medio <= medio) :', grande > medio <= medio)
print('pequeno >= pequeno < grande :', pequeno >= pequeno < grande)
print('grande <= grande > medio :', grande <= grande > medio)
