# Bibliotecas
from random import randint

# Funções


def jogada_humana():
    """Permite o usuário colocar dois números e verifica se eles estão dentro dos parâmetros do tabuleiro do jogo da
    velha (Uma matriz 3x3). Após a verificação, retorna a coordenada que o usuário escreveu -1, para poder ser utilizado
    na iteração do tabuleiro."""

    try:
        linha = int(input('Insira os números posição você quer jogar, a ordem é Linha e Coluna\nNúmero da linha: '))
        while linha < 1 or linha > 3:
            linha = int(input('Número de linha inválido! Digite novamente\nNúmero de linha: '))
    except ValueError:
        print('Deve ser colocado um número inteiro, e não uma string ou número fracionário (float).')
        return None

    try:
        coluna = int(input('\nNúmero da coluna: '))
        while coluna < 1 or coluna > 3:
            coluna = int(input('Número de coluna inválido! Digite novamente\nNúmero de coluna: '))
    except ValueError:
        print('Deve ser colocado um número inteiro, e não uma string ou número fracionário (float).')
        return None

    return linha - 1, coluna - 1


def jogada_computador(x):
    """Faz uma jogada aleatória do computador, escolhendo uma linha e uma coluna para formar a coordenada na matriz 3x3
    que representa o tabuleiro."""

    linha = randint(0, 2)
    coluna = randint(0, 2)
    while x[linha][coluna] != '*':
        linha = randint(0, 2)
        coluna = randint(0, 2)
    return linha, coluna


def mostrar_tabuleiro(z):
    """Função que mostra a matriz 3x3 que representa o tabuleiro"""
    [[print(x, end='\t\t', flush=True) for x in y] and print('\n') for y in z]
    print('\n')


def vitoria_linha(z):
    """Verifica a vitória do usuário pela linha."""

    if z[0][0] == z[0][1] == z[0][2] == 'X' or z[0][0] == z[0][1] == z[0][2] == 'O':
        return True, z[0][0]
    elif z[1][0] == z[1][1] == z[1][2] == 'X' or z[1][0] == z[1][1] == z[1][2] == 'O':
        return True, z[1][0]
    elif z[2][0] == z[2][1] == z[2][2] == 'X' or z[2][0] == z[2][1] == z[2][2] == 'O':
        return True, z[2][0]
    return False


def vitoria_coluna(z):
    """Verifica a vitória do usuário pela coluna."""

    if z[0][0] == z[1][0] == z[2][0] == 'X' or z[0][0] == z[1][0] == z[2][0] == 'O':
        return True, z[0][0]
    elif z[0][1] == z[1][1] == z[2][1] == 'X' or z[0][1] == z[1][1] == z[2][1] == 'O':
        return True, z[0][1]
    elif z[0][2] == z[1][2] == z[2][2] == 'X' or z[0][2] == z[1][2] == z[2][2] == 'O':
        return True, z[0][2]
    return False


def vitoria_diagonal(z):
    """Verifica a vitória do usuário pela diagonal."""

    if z[0][0] == z[1][1] == z[2][2] == 'X' or z[0][0] == z[1][1] == z[2][2] == 'O':
        return True, z[0][0]
    elif z[0][2] == z[1][1] == z[2][0] == 'X' or z[0][2] == z[1][1] == z[2][0] == 'O':
        return True, z[0][2]
    return False


def tie(z):
    """Verifica se houve empate ou não."""

    for y in z:
        velha = any(x == '*' for x in y)
        if velha:
            return False
    return True


# Variáveis para o uso no jogo
tabuleiro = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
vez = 0
win = False

# Apresentação, escolha do modo de jogo e de quem jogará primeiro: X ou O
print('Este é um jogo da velha. Para jogar, você deve inserir o número da linha e da coluna em que quer jogar.\n')
pvp = int(input('Digite a escolha de modo de jogo:\n1. Jogar contra outra pessoa\n2. Jogar contra o computador\n'))
while pvp != 1 and pvp != 2:
    pvp = int(input('NÚMERO INVÁLIDO! Digite novamente a escolha de modo de jogo:\n1. Jogar contra outra pessoa\n'
                    '2. Jogar contra o computador\n'))

primeira_escolha = input('A primeira jogada será X ou O? ').upper()
while primeira_escolha != 'X' and primeira_escolha != 'O':
    primeira_escolha = input('ESCOLHA INVÁLIDA! Digite novamente\nA primeira jogada será X ou O? ').upper()

if primeira_escolha == 'X':
    segunda_escolha = 'O'
else:
    segunda_escolha = 'X'

# Lógica do jogo
mostrar_tabuleiro(tabuleiro)

while not win:
    # Modo jogador contra jogador
    if pvp == 1:
        jogada = jogada_humana()

        # Se a vez for um número par, será jogado o X. Se for ímpar, será jogado o O.

        if vez % 2 == 0:
            try:
                while tabuleiro[jogada[0]][jogada[1]] != '*':
                    print('ERRO. A casa já está ocupada! Digite outra coordenada!')
                    jogada = jogada_humana()
                tabuleiro[jogada[0]][jogada[1]] = f'{primeira_escolha}'
            except TypeError:
                vez = 1
                print('Jogue novamente!\n')
        else:
            try:
                while tabuleiro[jogada[0]][jogada[1]] != '*':
                    print('ERRO. A casa já está ocupada! Digite outra coordenada!')
                    jogada = jogada_humana()
                tabuleiro[jogada[0]][jogada[1]] = f'{segunda_escolha}'
            except TypeError:
                vez = 0
                print('Jogue novamente!\n')

        # Uso da funções para verificar a vitória ou empate e mostrar o tabuleiro, além da adição da variável
        # vez para controle das jogadas.
        vez = vez + 1
        mostrar_tabuleiro(tabuleiro)
        win_linha = vitoria_linha(tabuleiro)
        win_coluna = vitoria_coluna(tabuleiro)
        win_diagonal = vitoria_diagonal(tabuleiro)
        empate = tie(tabuleiro)

    # Modo jogador contra computador
    else:
        if vez % 2 == 0:
            jogada = jogada_humana()
            try:
                while tabuleiro[jogada[0]][jogada[1]] != '*':
                    print('ERRO. A casa já está ocupada! Digite outra coordenada!')
                    jogada = jogada_humana()
                tabuleiro[jogada[0]][jogada[1]] = f'{primeira_escolha}'
            except TypeError:
                vez = 1
                print('Jogue novamente!\n')

        else:
            jogada = jogada_computador(tabuleiro)
            tabuleiro[jogada[0]][jogada[1]] = f'{segunda_escolha}'

        # Uso da funções para verificar a vitória ou empate e mostrar o tabuleiro, além da adição da variável
        # vez para controle das jogadas.
        vez = vez + 1
        mostrar_tabuleiro(tabuleiro)
        win_linha = vitoria_linha(tabuleiro)
        win_coluna = vitoria_coluna(tabuleiro)
        win_diagonal = vitoria_diagonal(tabuleiro)
        empate = tie(tabuleiro)

    # Verificação da condição de vitória ou empate
    if win_linha or win_coluna or win_diagonal or empate:
        win = True

# Parabenização e apresentação do vencedor
if win_linha:
    print(f'Parabéns! O {win_linha[1]} venceu!')
elif win_diagonal:
    print(f'Parabéns! O {win_diagonal[1]} venceu!')
elif win_coluna:
    print(f'Parabéns! O {win_coluna[1]} venceu!')
else:
    print('Deu velha!')
