from csv import DictReader, reader

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
    nomeCidade = codMunic[cidade][1][3::].title()
    numeroMunicUbs.append({'Estado': nomeEstado, 'Cidade': nomeCidade, 'Qntd': countUbs})

for contador in range(len(numeroMunicUbs)):  # Imprime o resultado na tela
    print(f"Estado: {numeroMunicUbs[contador]['Estado']}\tCidade: {numeroMunicUbs[contador]['Cidade']}\t"
          f"Número de UBS: {numeroMunicUbs[contador]['Qntd']}")
