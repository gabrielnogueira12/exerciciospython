import lol_project.functions.functions as func

print(func.find('blueTeamTag', 'NALCS', 2018, 'Spring', 'Season'))
x = func.find_matches('NALCS', 2018, 'TL')
for y in x:
    print(y)
# print(func.find('redTeamTag', 'CBLoL', 2017, 'Spring', 'Season', 'RED'))
