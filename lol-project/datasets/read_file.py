import pandas as pd

df_notuse = pd.read_csv('datasets\\matchinfo.csv')

columns = ['League', 'Year', 'Season', 'Type', 'blueTeamTag', 'redTeamTag', 'bResult', 'rResult', 'gamelength',
           'blueTop', 'blueTopChamp', 'blueJungle', 'blueJungleChamp', 'blueMiddle', 'blueMiddleChamp', 'blueADC',
           'blueADCChamp', 'blueSupport', 'blueSupportChamp', 'redTop', 'redTopChamp', 'redJungle', 'redJungleChamp',
           'redMiddle', 'redMiddleChamp', 'redADC', 'redADCChamp', 'redSupport', 'redSupportChamp', 'Address']
# Formata a tabela para que possa reorganizar a posição da coluna redTeamTag
df = df_notuse.reindex(columns=columns)

