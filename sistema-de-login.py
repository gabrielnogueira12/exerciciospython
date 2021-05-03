# Funções


def verification(user, password, users):
    """Recebe os argumentos user (representando o usuário), password (representando a senha) e users (que representa
    os usuários cadastrados). A função verifica se o usuário e senha digitados estão cadastrados juntos na lista de
    usuários."""

    for count in range(0, len(users)):
        if user == users[count]['Username'] and password == users[count]['Password']:
            return True
    return False


# Lista para cadastro dos usuários e variável para controle do menu.
users = []
menu = True

# Mostrando ao usuário as opções
while menu:
    menu = input('Escolha sua opção:\n1. Cadastrar novo usuário\n2. Fazer login\n3. Sair\n')

    # Cadastro de usuários
    if menu == '1':
        id_user = {'Username': input('Digite o seu username: '), 'Password': input('Digite sua senha: ')}
        users.append(id_user)

    # Tentativa de login e verificação da autenticação. Caso o login seja efetuado, já sei imediatamente do menu.
    elif menu == '2':
        username_login = input('Digite seu username: ')
        password_login = input('Digite sua senha: ')
        verif = verification(username_login, password_login, users)
        error = 0  # Variável para contagem de erros. Limite são 3 tentativas de login.
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

    # Saída do menu
    else:
        menu = False
