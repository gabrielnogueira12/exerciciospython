from lol_project.functions.functions import adjust_df, show_match
from lol_project.helper.leagues import ligas
from time import sleep

print('============================================')
print('================= Welcome! =================')
print('============================================')
print('You can access info of any profissional League of Legends match!')

choices = []  # Variable that will be used in the function to find the match
# Showing the leagues to the user
count = 1
for liga in ligas:
    print(f'{count}. {liga}')
    count += 1

# Choosing the league
choice_league = input('Choose the league: ')
choices.append(choice_league)

years = adjust_df(choice_league, 1)  # Getting the years of the choosen league
sleep(1)

# Showing the years to the user
count = 1
for year in years[0]:
    print(f'{count}. {year}')
    count += 1

# Choosing the year
choice_year = int(input('Choose the year: '))  # Needs to be integer
choices.append(choice_year)

seasons = adjust_df(tuple(choices), len(choices))  # Getting the season of the choosen year
sleep(1)

# Showing the seasons to the user
count = 1
for season in seasons[0]:
    print(f'{count}. {season}')
    count += 1

# Choosing the season
choice_season = input('Choose the season: ')
choices.append(choice_season)

type_seasons = adjust_df(tuple(choices), len(choices))  # Getting the type of the choosen season
sleep(1)

# Showing the type of the seasons to the user
count = 1
for type_season in type_seasons[0]:
    print(f'{count}. {type_season}')
    count += 1

# Choosing the type of the season
choice_type = input('Choose the year: ')
choices.append(choice_type)

first_team = adjust_df(tuple(choices), len(choices))  # Getting the first team of the choosen split
sleep(1)

# Showing the first team to the user
count = 1
for team in first_team[0]:
    print(f'{count}. {team}')
    count += 1

# Choosing the first team
choice_fteam = input('Choose the first team: ')
choices.append(choice_fteam)

second_team = adjust_df(tuple(choices), len(choices))  # Getting the others teams of the choosen split
sleep(1)

# Showing the second team to the user
count = 1
for team in second_team[0]:
    print(f'{count}. {team}')
    count += 1

# Choosing the second team
choice_steam = input('Choose the second team: ')
choices.append(choice_steam)

chosen_df = adjust_df(tuple(choices), len(choices))  # Getting the choosen match

show_match(chosen_df[1])  # Showing the informations about the choosen match
