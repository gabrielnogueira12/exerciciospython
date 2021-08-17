from lol_project.datasets.read_file import df, columns


def adjust_df(item_chosen, tam):
    """Adjust a dataframe to get the info about the choosen itens in the original dataframe"""
    list_column = []
    for item in range(tam):
        list_column.append(columns[item])

    df2 = df.groupby(list_column)

    for column, dataf in df2:
        if column == item_chosen:
            df3 = dataf

    df4 = df3.groupby(columns[len(list_column)])

    set_next = set()
    for column, dataf in df4:
        set_next.add(column)

    return set_next, df3


def show_match(chosen_df):
    """Show the information about the choosen match"""
    print('\n\n============== MATCH INFO ==============')
    print(f"League: {chosen_df.iloc[0]['League']}")

    print(f"Year: {chosen_df.iloc[0]['Year']}")

    print(f"Season: {chosen_df.iloc[0]['Season']}")

    print(f"Year: {chosen_df.iloc[0]['Type']}")

    print(f"Match: {chosen_df.iloc[0]['blueTeamTag']} x {chosen_df.iloc[0]['redTeamTag']}")

    if chosen_df.iloc[0]['bResult'] == 1:
        winner = chosen_df.iloc[0]['blueTeamTag']
        loser = chosen_df.iloc[0]['redTeamTag']
    else:
        loser = chosen_df.iloc[0]['blueTeamTag']
        winner = chosen_df.iloc[0]['redTeamTag']

    print(f'Winner team: {winner}\nLoser team: {loser}')

    print(f"Game Lenght: {chosen_df.iloc[0]['gamelength']} minutes\n")

    print(f"{chosen_df.iloc[0]['blueTeamTag']} INFO\n\nSide: Blue")
    print("Rolster".ljust(20), "-> Champion:")
    print("Top laner:".ljust(10), f"{chosen_df.iloc[0]['blueTop']}".ljust(10),
          f"-> {chosen_df.iloc[0]['blueTopChamp']}")
    print("Jungler:".ljust(10), f"{chosen_df.iloc[0]['blueJungle']}".ljust(10),
          f"-> {chosen_df.iloc[0]['blueJungleChamp']}")
    print("Mid laner:".ljust(10), f"{chosen_df.iloc[0]['blueMiddle']}".ljust(10),
          f"-> {chosen_df.iloc[0]['blueMiddleChamp']}")
    print("AD Carry:".ljust(10), f"{chosen_df.iloc[0]['blueADC']}".ljust(10),
          f"-> {chosen_df.iloc[0]['blueADCChamp']}")
    print("Support:".ljust(10), f"{chosen_df.iloc[0]['blueSupport']}".ljust(10),
          f"-> {chosen_df.iloc[0]['blueSupportChamp']}\n")

    print(f"{chosen_df.iloc[0]['redTeamTag']} INFO\n\nSide: Red")
    print("Rolster".ljust(21), "-> Champion:")
    print("Top laner:".ljust(10), f"{chosen_df.iloc[0]['redTop']}".ljust(10),
          f"-> {chosen_df.iloc[0]['redTopChamp']}")
    print("Jungler:".ljust(10), f"{chosen_df.iloc[0]['redJungle']}".ljust(10),
          f"-> {chosen_df.iloc[0]['redJungleChamp']}")
    print("Mid laner:".ljust(10), f"{chosen_df.iloc[0]['redMiddle']}".ljust(10),
          f"-> {chosen_df.iloc[0]['redMiddleChamp']}")
    print("AD Carry:".ljust(10), f"{chosen_df.iloc[0]['redADC']}".ljust(10),
          f"-> {chosen_df.iloc[0]['redADCChamp']}")
    print("Support:".ljust(10), f"{chosen_df.iloc[0]['redSupport']}".ljust(10),
          f"-> {chosen_df.iloc[0]['redSupportChamp']}\n")
