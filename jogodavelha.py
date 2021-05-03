from random import randint

tabuleiro = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]


def jogada_humana():
    print('Insira os números posição você quer jogar, a ordem é Linha e Coluna\n')
    linha = int(input('Número da linha: '))
    while linha < 1 or linha > 3:
        linha = int(input('Número de linha inválido! Digite novamente\nNúmero de linha: '))
    coluna = int(input('\nNúmero da coluna: '))
    while coluna < 1 or coluna > 3:
        coluna = int(input('Número de coluna inválido! Digite novamente\nNúmero de coluna: '))
    return linha-1, coluna-1


def jogada_computador(x):
    linha = randint(0, 2)
    coluna = randint(0, 2)
    while x[linha][coluna] != '*':
        linha = randint(0, 2)
        coluna = randint(0, 2)
    return linha, coluna


def mostrar_tabuleiro(z):
    [[print(x, end='\t\t', flush=True) for x in y] and print('\n') for y in z]


def vitoria_linha(z):
    if z[0][0] == z[0][1] == z[0][2] == 'X' or z[0][0] == z[0][1] == z[0][2] == 'O':
        return True, z[0][0]
    elif z[1][0] == z[1][1] == z[1][2] == 'X' or z[1][0] == z[1][1] == z[1][2] == 'O':
        return True, z[1][0]
    elif z[2][0] == z[2][1] == z[2][2] == 'X' or z[2][0] == z[2][1] == z[2][2] == 'O':
        return True, z[2][0]
    return False


def vitoria_coluna(z):
    if z[0][0] == z[1][0] == z[2][0] == 'X' or z[0][0] == z[1][0] == z[2][0] == 'O':
        return True, z[0][0]
    elif z[0][1] == z[1][1] == z[2][1] == 'X' or z[0][1] == z[1][1] == z[2][1] == 'O':
        return True, z[0][1]
    elif z[0][2] == z[1][2] == z[2][2] == 'X' or z[0][2] == z[1][2] == z[2][2] == 'O':
        return True, z[0][2]
    return False


def vitoria_diagonal(z):
    if z[0][0] == z[1][1] == z[2][2] == 'X' or z[0][0] == z[1][1] == z[2][2] == 'O':
        return True, z[0][0]
    elif z[0][2] == z[1][1] == z[2][0] == 'X' or z[0][2] == z[1][1] == z[2][0] == 'O':
        return True, z[0][2]
    return False


def tie(z):
    for y in z:
        velha = any(x == '*' for x in y)
        if velha:
            return False
    return True


vez = 0
win = False

print('Este é um jogo da velha. Para jogar, você deve inserir o número da linha e da coluna em que quer jogar.\n')
pvp = int(input('Digite a escolha de modo de jogo:\n1. Jogar contra outra pessoa\n2. Jogar contra o computador\n'))
while pvp != 1 and pvp != 2:
    pvp = int(input('NÚMERO INVÁLIDO! Digite novamente a escolha de modo de jogo:\n1. Jogar contra outra pessoa\n'
                    '2. Jogar contra o computador\n'))

mostrar_tabuleiro(tabuleiro)

while not win:
    if pvp == 1:
        print('A primeira pessoa a jogar será o X, e a segunda será o O. Boa sorte e se divirta!')

        jogada = jogada_humana()

        if vez % 2 == 0:
            while tabuleiro[jogada[0]][jogada[1]] != '*':
                print('ERRO. A casa já está ocupada! Digite outra coordenada!')
                jogada = jogada_humana()
            tabuleiro[jogada[0]][jogada[1]] = 'X'

        else:
            while tabuleiro[jogada[0]][jogada[1]] != '*':
                print('ERRO. A casa já está ocupada! Digite outra coordenada!')
                jogada = jogada_humana()
            tabuleiro[jogada[0]][jogada[1]] = 'O'

        vez = vez + 1
        mostrar_tabuleiro(tabuleiro)
        win_linha = vitoria_linha(tabuleiro)
        win_coluna = vitoria_coluna(tabuleiro)
        win_diagonal = vitoria_diagonal(tabuleiro)
        empate = tie(tabuleiro)

    else:
        if vez % 2 == 0:
            jogada = jogada_humana()
            while tabuleiro[jogada[0]][jogada[1]] != '*':
                print('ERRO. A casa já está ocupada! Digite outra coordenada!')
                jogada = jogada_humana()
            tabuleiro[jogada[0]][jogada[1]] = 'X'

        else:
            jogada = jogada_computador(tabuleiro)
            tabuleiro[jogada[0]][jogada[1]] = 'O'

        vez = vez + 1
        mostrar_tabuleiro(tabuleiro)
        win_linha = vitoria_linha(tabuleiro)
        win_coluna = vitoria_coluna(tabuleiro)
        win_diagonal = vitoria_diagonal(tabuleiro)
        empate = tie(tabuleiro)

    if win_linha or win_coluna or win_diagonal or empate:
        win = True


if win_linha:
    print(f'Parabéns! O {win_linha[1]} venceu!')
elif win_diagonal:
    print(f'Parabéns! O {win_diagonal[1]} venceu!')
elif win_coluna:
    print(f'Parabéns! O {win_coluna[1]} venceu!')
else:
    print('Deu velha!')
