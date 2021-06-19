from passlib.hash import pbkdf2_sha256 as cryp
import datetime


class User:
    idCount = 0
    usersbank = [{'username': None, 'password': None, 'id': None, 'completeName': None, 'birthdayDate': None,
                  'gender': None, 'email': None}]

    def __init__(self):
        self.username = None
        self.__password = None
        self.completename = None
        self.birthday = None
        self.gender = None
        self.email = None
        self.id = None

    def user_register(self):
        """Register an user in the system"""
        self.username = input('\nDigite seu nome de usuário: ')

        # Checking if the user isn't already registered in the system
        username_control = True
        for contador in range(len(User.usersbank)):  # If registered
            if User.usersbank[contador]['username'] == self.username:
                username_control = False
        if username_control is False:
            while username_control is False:
                for contador in range(len(User.usersbank)):  # If registered
                    if User.usersbank[contador]['username'] == self.username:
                        print('Nome de usuário já cadastrado! Tente novamente\n')
                        username_control = False
                        self.username = input('\nDigite seu nome de usuário: ')
                    else:  # If doesn't registered
                        username_control = True

        print('Nome de usuário válido!\n')

        # Controlling password
        password = input('Digite sua senha (Deve conter entre 8 e 16 dígitos): ')
        while len(password) < 8 or len(password) > 16:
            password = input('Senha inválida! Digite novamente sua senha (Deve conter entre 8 e 16 dígitos): ')
        self.__password = cryp.hash(password, rounds=20000, salt_size=16)

        self.completename = input('\nDigite o seu nome completo: ')

        # Controlling birthday date
        birthdaydate = input('\nDigite sua data de nascimento (dd/mm/aaaa): ')

        birthday_loop = True
        while birthday_loop:
            birthday_control = birthdaydate.split('/')
            if len(birthday_control) == 3:
                try:
                    if len(birthday_control[0]) == 2 and len(birthday_control[1]) == 2 and \
                            len(birthday_control[2]) == 4:
                        if int(birthday_control[0]) <= 0 or int(birthday_control[0]) > 31:
                            birthdaydate = input(
                                'Data inválida! Digite novamente sua data de nascimento (dd/mm/aaaa): ')
                        else:
                            if int(birthday_control[1]) <= 0 or int(birthday_control[1]) > 12:
                                birthdaydate = input(
                                    'Data inválida! Digite novamente sua data de nascimento (dd/mm/aaaa): ')
                            else:
                                if int(birthday_control[2]) < 0:
                                    birthdaydate = input(
                                        'Data inválida! Digite novamente sua data de nascimento (dd/mm/aaaa): ')
                                else:
                                    birthday_loop = False
                    else:
                        birthdaydate = input(
                            'Data inválida! Digite novamente sua data de nascimento (dd/mm/aaaa): ')
                except ValueError:
                    birthdaydate = input('Data inválida! Digite novamente sua data de nascimento (dd/mm/aaaa): ')
            else:
                birthdaydate = input('Data inválida! Digite novamente sua data de nascimento (dd/mm/aaaa): ')

        self.birthday = datetime.datetime.strptime(birthdaydate, '%d/%m/%Y')

        # Controlling gender
        self.gender = input('\nDigite seu gênero (M/F): ').upper()
        while self.gender != 'M' and self.gender != 'F':
            self.gender = input('Escolha inválida! Digite novamete seu gênero (M/F): ').upper()

        # Controlling email
        self.email = input('\nDigite seu email: ')
        if len(self.email.split('@')) != 2:
            self.email = input('Email inválido! Digite novamente seu email: ')

        # id
        self.id = User.idCount
        User.idCount += 1

        # Adding the new user on the system
        User.usersbank.append({'username': self.username, 'password': self.__password, 'id': self.id,
                               'completeName': self.completename, 'birthdayDate': self.birthday,
                               'gender': self.gender, 'email': self.email})


def login(username, password):
    """Check if the user and password are registered in the system and allow or not the login"""
    for contador in range(len(User.usersbank)):  # If exists
        if User.usersbank[contador]['username'] == username:
            if cryp.verify(password, User.usersbank[contador]['password']):
                print('Login bem sucedido!')
                return True
    print('Usuário e/ou senha inválido(s)!')
    return False


def check_user(username):
    """Print the informations of the user named"""
    for contador in range(len(User.usersbank)):  # If exists
        if User.usersbank[contador]['username'] == username:
            print(f'Nome de usuário: {User.usersbank[contador]["username"]}\n'
                  f'Nome completo: {User.usersbank[contador]["completeName"]}\n'
                  f'Data de nascimento: {User.usersbank[contador]["birthdayDate"].day}/'
                  f'{User.usersbank[contador]["birthdayDate"].month}/{User.usersbank[contador]["birthdayDate"].year}\n'
                  f'Gênero: {User.usersbank[contador]["gender"]}\n'
                  f'Email: {User.usersbank[contador]["email"]}')
            return True
    print('Usuário não cadastrado!')  # If doesn't exist


def change_user(username):
    """Allow the user change their information"""
    for contador in range(len(User.usersbank)):  # If exists
        if User.usersbank[contador]['username'] == username:
            print(f'Seus dados atuais são:\n'
                  f'Nome de usuário: {User.usersbank[contador]["username"]}\n'
                  f'Nome completo: {User.usersbank[contador]["completeName"]}\n'
                  f'Data de nascimento: {User.usersbank[contador]["birthdayDate"]}\n'
                  f'Gênero: {User.usersbank[contador]["gender"]}\n'
                  f'Email: {User.usersbank[contador]["email"]}\n')

            # Changing username
            new_username = input('Digite o nome de usuário: ')
            username_control = True
            for contador2 in range(len(User.usersbank)):  # If registered
                if User.usersbank[contador2]['username'] == new_username:
                    username_control = False
            if username_control is False:
                while username_control is False:
                    for contador2 in range(len(User.usersbank)):  # If registered
                        if User.usersbank[contador2]['username'] == new_username:
                            print('Nome de usuário já cadastrado! Tente novamente\n')
                            username_control = False
                            new_username = input('\nDigite seu nome de usuário: ')
                        else:  # If doesn't registered
                            username_control = True
            User.usersbank[contador]['username'] = new_username
            print('Nome de usuário válido!\n')

            # Changing name
            User.usersbank[contador]["completeName"] = input('Digite o nome: ')

            # Changing birthday date
            new_birthdaydate = input('Digite a data de aniverário (dd/mm/aaaa): ')
            birthday_loop = True
            while birthday_loop:
                birthday_control = new_birthdaydate.split('/')
                if len(birthday_control) == 3:
                    try:
                        if len(birthday_control[0]) == 2 and len(birthday_control[1]) == 2 and \
                                len(birthday_control[2]) == 4:
                            if int(birthday_control[0]) <= 0 or int(birthday_control[0]) > 31:
                                new_birthdaydate = input(
                                    'Data inválida! Digite novamente sua data de nascimento (dd/mm/aaaa): ')
                            else:
                                if int(birthday_control[1]) <= 0 or int(birthday_control[1]) > 12:
                                    new_birthdaydate = input(
                                        'Data inválida! Digite novamente sua data de nascimento (dd/mm/aaaa): ')
                                else:
                                    if int(birthday_control[2]) < 0:
                                        new_birthdaydate = input(
                                            'Data inválida! Digite novamente sua data de nascimento (dd/mm/aaaa): ')
                                    else:
                                        birthday_loop = False
                        else:
                            new_birthdaydate = input(
                                'Data inválida! Digite novamente sua data de nascimento (dd/mm/aaaa): ')
                    except ValueError:
                        new_birthdaydate = input(
                            'Data inválida! Digite novamente sua data de nascimento (dd/mm/aaaa): ')
                else:
                    new_birthdaydate = input('Data inválida! Digite novamente sua data de nascimento (dd/mm/aaaa): ')
            new_birthdaydate_format = datetime.datetime.strptime(new_birthdaydate, '%d/%m/%Y')
            User.usersbank[contador]["birthdayDate"] = new_birthdaydate_format

            # New gender
            new_gender = input('Digite o gênero (M/F): ')
            while new_gender != 'M' and new_gender != 'F':
                new_gender = input('Escolha inválida! Digite novamete seu gênero (M/F): ').upper()
            User.usersbank[contador]["gender"] = new_gender

            # New email
            new_email = input('Digite o email: ')
            if len(new_email.split('@')) != 2:
                new_email = input('Email inválido! Digite novamente seu email: ')
            User.usersbank[contador]["email"] = new_email

            return new_username
        else:
            print('Usuário não cadastrado!')  # If doesn't exist


print('================================================'.center(50))
print('Bem vindo ao sistema de usuário'.center(50))
print('================================================'.center(50))

# Showing the menu
menu_nolog = True
loggedin = False

while menu_nolog:
    menu_option = input('Escolha uma opção do menu para continuar\nMENU DE OPÇÕES:\n1. Fazer login\n'
                        '2. Cadastrar novo usuário\n3. Sair\n')

    while menu_option != '1' and menu_option != '2' and menu_option != '3':
        menu_option = input('ESCOLHA INVÁLIDA\nMENU DE OPÇÕES:\n1. Fazer login\n'
                            '2. Cadastrar novo usuário\n3. Sair\n')

    # Making login
    if menu_option == '1':
        errorCount = 0  # Count the mistakes when fail login
        errorKick = False  # Mark if exceeded the mistakes
        usernameLog = input('\nDigite o nome de usuário: ')
        passwordLog = input('Digite a senha: ')

        tryinglog = login(usernameLog, passwordLog)

        while tryinglog is False and errorCount < 2:
            errorCount += 1
            usernameLog = input('\nDigite o nome de usuário: ')
            passwordLog = input('Digite a senha: ')
            tryinglog = login(usernameLog, passwordLog)
        if errorCount == 2:
            errorKick = True
        if errorKick:
            print('\nTentativas de login excedidas! Tente novamente depois.')
            menu_nolog = False
        else:
            loggedin = True
            menu_nolog = False

    elif menu_option == '2':
        userLog = User()
        userLog.user_register()
        print('\nUsuário cadastrado com sucesso! Faça o login para continuar.\n\n')

    else:
        menu_nolog = False

# User logged in the system
while loggedin:
    menu_log_option = input('\n\nVocê está dentro do sistema! Escolha uma opção do menu:\n'
                            '1. Consultar seus dados\n2. Alterar seus dados\n3. Sair\n')

    while menu_log_option != '1' and menu_log_option != '2' and menu_log_option != '3':
        menu_log_option = input('ESCOLHA INVÁLIDA! Escolha uma opção do menu:\n'
                                '1. Consultar seus dados\n2. Alterar seus dados\n3. Sair\n')

    if menu_log_option == '1':
        check_user(usernameLog)

    elif menu_log_option == '2':
        usernameLog = change_user(usernameLog)

    else:
        loggedin = False
