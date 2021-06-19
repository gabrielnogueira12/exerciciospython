from lol_project.datasets.read_file import df

ligas = set()
for item in df['League'].items():
    ligas.add(item[1])