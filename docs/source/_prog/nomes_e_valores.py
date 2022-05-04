PI = 3.1416
nome_para_um = 1
outro_nome_para_um = 1
era_um_vira_dois = 1
print('nome_para_um, outro_nome_para_um, era_um_vira_dois, o PI:')
print(nome_para_um, outro_nome_para_um, era_um_vira_dois, PI)
era_um_vira_dois = 2
print('nome_para_um, outro_nome_para_um, era_um_vira_dois:')
print(nome_para_um, outro_nome_para_um, era_um_vira_dois)
# nome_para_um e outro_nome_para_um continuam, era_um_vira_dois agora é nome para dois
era_numero_vira_texto = 1
print('era_numero_vira_texto:', era_numero_vira_texto)
era_numero_vira_texto = "um texto"
print('era_numero_vira_texto:', era_numero_vira_texto)
# o nome não está preso para ser um um número pode ser outra coisa
nome_para_um = outro_nome_para_um = 1
# outra maneira de colocar dois nomes em um valor
print('nome_para_um:', nome_para_um, 'outro_nome_para_um:', outro_nome_para_um)
nome_para_um = 1
outro_nome_para_um = nome_para_um
# mais uma maneira de colocar dois nomes em um valor
print('nome_para_um:', nome_para_um, 'outro_nome_para_um:', outro_nome_para_um)
nome_para_um, nome_para_dois = 1, 2
# outra maneira de colocar dois nomes em dois valores
print('nome_para_um:', nome_para_um, 'nome_para_dois:', nome_para_dois)
um_vira_dois, dois_vira_um = 1, 2
# um_vira_dois, dois_vira_um nomeiam respectivamente 1 e 2
print('um_vira_dois:', um_vira_dois, 'dois_vira_um:', dois_vira_um)
um_vira_dois, dois_vira_um = dois_vira_um, um_vira_dois
# agora eles trocaram, um_vira_dois agora nomeia o valor nomeado pelo dois_vira_um
print('um_vira_dois:', um_vira_dois, 'dois_vira_um:', dois_vira_um)


class FazNada:
    ...  # este símbolo ... conclui a declaração avisando que ainda não foi definida
    # segundo a PEP8 devemos colocar duas linhas em branco antes e depois de uma classe


print("este é o tipo FazNada", FazNada)
