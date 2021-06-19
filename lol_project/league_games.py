import lol_project.functions.functions as func
from lol_project.helper.leagues import ligas
from time import sleep

print('=========================================')
print('========== Bem-vindo, usuário! ==========')
print('=========================================')
print('Neste programa, você pode acessar os dados das partidas de ligas profissionais de League of Legends!')

# Mostrando as ligas para o usuário
count = 1
for liga in ligas:
    print(f'{count}. {liga}')
    count += 1

# Escolha da liga
choice_league = input('\nEscolha o nome da liga que você deseja consultar: ')
sleep(1)

# Mostrando os anos
years = func.find('Year', choice_league)
count = 1

for year in years:
    print(f'{count}. {year}')
    count += 1

# Escolha do ano
choice_year = input('\nEscolha o ano da liga que você deseja consultar: ')
sleep(1)

# Mostrando os splits
splits = func.find('Season', choice_league, int(choice_year))
count = 1

for split in splits:
    print(f'{count}. {split}')
    count += 1

# Escolha do split
choice_split = input('\nEscolha o split da liga que você deseja cosultar: ')
sleep(1)

# Mostrando os times
teams = func.find('blueTeamTag', choice_league, int(choice_year), choice_split, 'Season')
count = 1

for team in teams:
    print(f'{count}. {team}')
    count += 1

# Escolha do time
choice_team = input('\nEscolha o time que você deseja ver os confrontos: ')
sleep(1)

# Mostrando os confrontos
games = func.find_matches(choice_league, int(choice_year), choice_team)

for game in games:
    print(game)

