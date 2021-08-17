import sistemadeusuario
from csv import DictWriter

with open('bancodeusuarios.csv', 'w') as arquivo:
    cabecalho = sistemadeusuario.User.usersbank[0].keys()
    escrever_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escrever_csv.writeheader()
    for usuario in sistemadeusuario.User.usersbank:
        escrever_csv.writerow({'username': usuario['username'],
                               'password': usuario['password'],
                               'id': usuario['id'],
                               'completeName': usuario['completeName'],
                               'birthdayDate': usuario['birthdayDate'],
                               'gender': usuario['gender'],
                               'email': usuario['email']})