from lol_project.helper.format_df import format_df


def find(value, *args):
    """Procura os valores dos índices de value, formatando a tabela para poder encontrar"""
    try:
        df2 = format_df(args)
        df2_value_item = df2[value].items()
        rep_of_value = set()  # Conjunto com os valores encontrados
        for item in df2_value_item:
            rep_of_value.add(item[1])
        return rep_of_value
    except TypeError:
        return None


def find_matches(league, year, blueteam):
    """Procura os adversários contra quem o time fornecido no blueteam jogou no ano dado"""
    season = find('Season', league, year)
    matches = []
    for s in season:
        type_season = find('Type', league, year, s)

        for t in type_season:
            redteams = find('redTeamTag', league, year, s, t, blueteam)

            try:
                for team in redteams:
                    matches.append(f"{blueteam} x {team} | {s} - {t}")
            except TypeError:
                pass
    return matches
