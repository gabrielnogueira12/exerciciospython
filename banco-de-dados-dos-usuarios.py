from csv import reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    for linha in leitor_csv:
        print(f'{linha[0]} | {linha[1]} | {linha[2]}')