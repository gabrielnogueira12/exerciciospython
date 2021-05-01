def verification(user, password, users):
    for count in range(0, len(users)):
        if user == users[count]['Username'] and password == users[count]['Password']:
            return True
    return False


users = []

menu = True

while menu:
    menu = input('Escolha sua opção:\n1. Cadastrar novo usuário\n2. Fazer login\n3. Sair\n')

    if menu == '1':
        id_user = {'Username': input('Digite o seu username: '), 'Password': input('Digite sua senha: ')}
        users.append(id_user)

    elif menu == '2':
        username_login = input('Digite seu username: ')
        password_login = input('Digite sua senha: ')
        verif = verification(username_login, password_login, users)
        error = 0
        while not verif and error < 2:
            error = error + 1
            print('Usuário e/ou senha inválidos! Faça o login novamente')
            username_login = input('Digite seu username: ')
            password_login = input('Digite sua senha: ')
            verif = verification(username_login, password_login, users)
        if error == 2 and not verif:
            print('Você excedeu o número de tentativas! Tente novamente mais tarde.')
        else:
            print('Login bem sucedido!')
        menu = False

    else:
        menu = False