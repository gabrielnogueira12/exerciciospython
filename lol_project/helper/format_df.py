import lol_project.datasets.read_file as rd


def format_df(lista, df=rd.df):
    """Formata o dataframe para que possa trabalhar com o dado que eu quero nos índices"""
    try:
        df_columns = list(df.columns)
        for time in range(len(lista)):
            df2 = df.set_index(df_columns[time]).loc[lista[time]]
            df = df2
        return df2
    except KeyError:
        return None
