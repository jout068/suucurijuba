_SET0_ = {
    "script_name": "dojo_pre_0",
    "script_div_id": "dojo_pre_0",
    "height": 100, "index": "0.1", "title": "use como calculadora"
}  # _SEC_
print("soma 1 + 2: ", 1+2)
print("subtrai 2 - 1: ", 2-1)
print("divide 4 / 2: ", 4/2)
print("multiplica 3 x 2: ", 3*2)

_SET1_ = {
    "script_name": "dojo_pre_1",
    "script_div_id": "dojo_pre_1",
    "height": 150, "index": "0.2", "title": "use a memória"
}  # _SEC_
soma_um_mais_dois = 1+2
subtrai_um_de_dois = 2-1
divide_quatro_por_dois = 4/2
multiplica_tres_vezes_dois = 3*2
print("soma 1 + 2: ", soma_um_mais_dois)
print("subtrai 2 - 1: ", subtrai_um_de_dois)
print("divide 4 / 2: ", divide_quatro_por_dois)
print("multiplica 3 x 2: ", multiplica_tres_vezes_dois)

_SET2_ = {
    "script_name": "dojo_pre_2",
    "script_div_id": "dojo_pre_2",
    "height": 150, "index": "0.3", "title": "use uma lista"
}  # _SEC_
numeros_2_9_7 = [2, 9, 7]
intervalo_0_a_3 = range(4)
lista_int_0_a_3 = list(intervalo_0_a_3)
lista_pulando_dois = list(range(0, 8, 2))
print("numeros 2, 9 e 7: ", numeros_2_9_7)
print("lista intervalo de 0 a 3: ", lista_int_0_a_3)
print("lista pulando de dois: ", lista_pulando_dois)
print("pulando de outro jeito: ", lista_int_0_a_3[::2])

_SET3_ = {
    "script_name": "dojo_pre_3",
    "script_div_id": "dojo_pre_3",
    "height": 150, "index": "0.4", "title": "use itens da lista"
}  # _SEC_
numeros_2_9_7 = [2, 9, 7]
intervalo_0_a_3 = range(4)
lista_int_0_a_3 = list(intervalo_0_a_3)
taboada_de_3 = [taboada * 3 for taboada in range(9)]
for num in numeros_2_9_7:
    print("um numero na lista: ", num)
for taboada in intervalo_0_a_3:
    print("taboada de 2: ", 2*taboada)
print("taboada de 3: ", taboada_de_3)

_SETA_ = {
    "script_name": "dojo_pre_3_1",
    "script_div_id": "dojo_pre_3_1",
    "height": 250, "index": "0.4.1", "title": "propriedades da lista"
}  # _SEC_
lista_int_0_a_9 = list(range(9))
item_4_da_lista = lista_int_0_a_9[3]  # inicia no zero
lista_ate_o_item_4 = lista_int_0_a_9[:4]  # exclui o quarto
lista_do_item_4_em_diante = lista_int_0_a_9[3:]
ultimo_item_da_lista = lista_int_0_a_9[-1]
do_penultimo_item_em_diante = lista_int_0_a_9[-2:]
print("uma cópia da lista: ", lista_int_0_a_9[:])
print("item 4 da lista: ", item_4_da_lista)
print("lista até o item_4: ", lista_ate_o_item_4)
print("lista do item 4 em diante: ", lista_do_item_4_em_diante)
print("último item da lista: ", ultimo_item_da_lista)
print("do penúltimo item em diante: ", do_penultimo_item_em_diante)

_SET4_ = {
    "script_name": "dojo_pre_4",
    "script_div_id": "dojo_pre_4",
    "height": 100, "index": "0.5", "title": "pondo texto no navegador"
}  # _SEC_
from browser import document
# O nome document aponta para uma lista das partes do navegador
parte = document["um_texto"]
# Aqui a lista vai retornar a parte que foi identificada por "um_texto"
parte.html = "Um texto que escrevi usando o programa Python"

_SET5_ = {
    "script_name": "dojo_pre_5",
    "script_div_id": "dojo_pre_5",
    "height": 300, "index": "0.6", "title": "desenhando coisas"
}  # _SEC_
from browser import document
from browser import svg
# O nome document aponta para uma lista das partes do navegador
parte = document["um_desenho"]
tela = svg.svg(width=400, height=200)
parte <= tela
# Aqui a parte vai receber uma tela de desenho criada com o tamanho 400x200
tela <= svg.rect(width=100, height=150, style={'fill': 'red'})
tela <= svg.circle(cx=200, cy=100, r=80, style={'fill': 'blue'})
tela <= svg.line(x1=110, y1=30, x2=120, y2=180, style={'stroke': 'green', 'stroke-width': '5px'})
tela <= svg.path(d="M320 20 l80 80 l-80 80 Z", style={'fill': 'magenta'})

_SET6_ = {
    "script_name": "dojo_pre_6",
    "script_div_id": "dojo_pre_6",
    "height": 300, "index": "0.7", "title": "desenhando arco-iris"
}  # _SEC_
from browser import document
from browser import svg
# O nome document aponta para uma lista das partes do navegador
parte = document["arco_iris"]
tela = svg.svg(width=400, height=200)
parte <= tela
# Aqui a parte vai receber uma tela de desenho criada com o tamanho 400x200
cores = 'cria aqui uma lista com as cores do arco iris'
# desenhe aqui o seu arco-iris usando um for

_SET7_ = {
    "script_name": "dojo_pre_7",
    "script_div_id": "dojo_pre_7",
    "height": 300, "index": "0.8", "title": "brincando de Volpi"
}  # _SEC_
from browser import document
from browser import svg
from random import choice
# O nome document aponta para uma lista das partes do navegador
parte = document["volpi"]
tela = svg.svg(width=400, height=200)
parte <= tela
# Aqui a parte vai receber uma tela de desenho criada com o tamanho 400x200
cores = 'cria aqui uma lista com as cores do arco iris'
# desenhe aqui o seu quadro de volpi usando um for e um "svg.path"
...
umacor = choice(cores)  # escolhe uma cor aleatória da lista de cores
# bla bla svg.path((d=f"M{x} {y} h40 v50 l-20 -20 l-20 20 v-40 Z", style={'fill': umacor}))
