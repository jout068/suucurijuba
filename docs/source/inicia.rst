.. _modulo_inicia:

Nomes e Valores em Python
============================

Um conceito elementar em programação é armazenar e lidar com valores que representam tudo que se quer computar.
Em um programa Python estes valores podem ser de diversos tipos e para lidar com eles colocamos nomes para
melhor lembrar o que representam.


.. code-block:: python

    tom = "um gato" # aqui o nome tom foi colocado para identificar o texto -um gato-
    jerry = "um rato" # aqui jerry indentifica o texto -um rato-
    num_bichos = 2 # onome num_bichos identifica o valor 2
    print("O desenho tem ", num_bichos, 'personagens: ' tom, "e ", jerry)
    # O texto impresso será: -O desenho tem 2 personagens: um gato e um rato-

A expressão *tom = "um gato"* quer dizer: use o nome *tom* para se referenciar ao texto *um gato*.
Diferentemente do uso em matemática o símbolo *=* não quer dizer igualdade.
No Python, o símbolo igual (**=**) quer dizer: atribua ao nome *tom* o valor *um gato*.
Em todo lugar que você colocar o nome tom, o Python vai substituir pelo seu valor *um gato*.
Funciona como na comunicação internet, onde você usa o emoji 😀 e o leitor entende que você na verdade
escreveu: *isto é engraçado*.
A expressão *<um nome> = <um valor>* no Python é chamada de atribuição.
Com ela declaramos que doravante este nome representa este valor indicado.

.. note::
    É importante ressaltar que um nome só poderá ser usado no programa se antes ele foi atribuído a um valor.

Existe umas regras de boas maneiras para escolher e escrever um nome em Python.
Estas regras foram definidas pela `Python Software Foundation <https://www.python.org/psf/>`_
em um documento chamado `PEP8 <https://peps.python.org/pep-0008/>`_.

Em sua maior parte os nomes devem ser escritos em letras minúsculas com as palavras separadas
pelo caracter *sublinhado(_)* por exemplo: *meu_gato*. Se o nome for se referir a uma constante,
isto é, se o seu valor nunca será trocado em todo o programa, então todas as letras serão em caixa alta.
Por exemplo *PT_BR = "Português do Brasil"*. Caso você vá definir um tipo novo que você criou,
a norma é usar o **PascalCase** ou **UpperCamelCase**, com todas as palavras grudadas e começadas em caixa alta.
Por exemplo, a palavra *class* em Python é usada para criar um tipo novo: *class GatoFrajola: <continua..>*

.. raw:: html

  <div id="nomes_e_valores"></div>
  <script type="text/python">
      from ScriptWidget import ScriptWidget
      sw2 = ScriptWidget(script_name="nomes_e_valores.py", main_div_id="nomes_e_valores", height=400, index="1.1", title="nomes e valores")
  </script>


.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

.. note::
   Procure ser cooperativo com a sua equipe.
