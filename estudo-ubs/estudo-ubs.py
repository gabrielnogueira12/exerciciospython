from csv import DictReader, reader
from os import system


def procura_cidade(lista, city, estado):
    for cont in lista:
        if cont['Cidade'].upper() == city.upper() and cont['Estado'].upper() == estado.upper():
            print(f"{cont['Cidade']} - {cont['Estado']} tem {cont['Qntd']} unidades básicas de saúde.")
            return True
    print('A cidade não se encontra na lista.')
    return False


with open('ubs.csv', encoding='utf-8') as ubs:  # Lê os dados sobre as UBS
    ler_ubs = DictReader(ubs)
    codUbs = []
    for contador in ler_ubs:
        codUbs.append(contador['cod_munic'])

with open('Lista_Municípios_com_IBGE_Brasil_Versao_CSV.csv') as municipio:  # Lê a lista de municípios do Brasil
    ler_munic = reader(municipio, delimiter=';')
    next(ler_munic)
    codMunic = []
    numMunic = 0
    for contador in ler_munic:
        codMunic.append([contador[1], contador[0]])
        numMunic += 1

numeroMunicUbs = []

for cidade in range(len(codMunic)):
    """Pega cada cidade da lista de municípios e faz a contagem de quantas vezes o código aparece na lista de UBS."""
    countUbs = 0
    for contador in codUbs:
        if contador == codMunic[cidade][0]:
            countUbs += 1
    nomeEstado = codMunic[cidade][1][0:2]
    nomeCidade = codMunic[cidade][1][2::].title()
    numeroMunicUbs.append({'Estado': nomeEstado, 'Cidade': nomeCidade, 'Qntd': countUbs})

controle_menu = True
while controle_menu is True:
    escolha_cidade = input("Digite o nome da cidade que você quer consultar ou digite 'SAIR': ")
    if escolha_cidade.upper() == 'SAIR':
        controle_menu = False
        break
    escolha_estado = input('Digite a sigla do estado em que está a cidade: ')
    procura_cidade(numeroMunicUbs, escolha_cidade, escolha_estado)

system('pause')
