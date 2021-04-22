from random import randint


def computador():
    x = randint(0, 3)
    if x == 0:
        return 'Papel'
    elif x == 1:
        return 'Pedra'
    return 'Tesoura'


def pessoa():
    x = input('Pedra, Papel ou Tesoura: ')
    return x.title()


def vencedor(x, y):
    if x == 'Pedra' and y == 'Tesoura':
        print('Você venceu!')
        return True
    elif x == 'Pedra' and y == 'Papel':
        print('Você perdeu!')
        return True
    elif x == 'Papel' and y == 'Tesoura':
        print('Você perdeu!')
        return True
    elif x == 'Papel' and y == 'Pedra':
        print('Você ganhou!')
        return True
    elif x == 'Tesoura' and y == 'Pedra':
        print('Você perdeu!')
        return True
    elif x == 'Tesoura' and y == 'Papel':
        print('Você ganhou!')
        return True
    else:
        print('Temos um empate! Jogue novamente')
        return False


win = False

while not win:
    jogadahumana = pessoa()
    jogadacomputador = computador()
    print(f'Você jogou: {jogadahumana}\nO computador jogou: {jogadacomputador}')
    win = vencedor(jogadahumana, jogadacomputador)
