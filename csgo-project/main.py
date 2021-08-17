from collections import Counter


def mostrar(x, y):
    print(f'Você tem R$ {y}')
    print('ITEM\tVALOR')
    for a, b in x.items():
        print(a, '\tR$', b)
    print('Para sair, digite: SAIR')


def dinheiro(x, y):
    return x - y


def verificar(x, y):
    for a in y.keys():
        if x.upper() == a.upper():
            return True, a
    return False


money = 8500

# CONJUNTO TR
armasTR = {'Ak-47': 2700, 'Galil-AR': 1800, 'AWP': 4750, 'SSG': 1100, 'MAC-10': 1100, 'P90': 2100}
pistolaTR = {'Glock': 0, 'P250': 300, 'Barretas Duplas': 400, 'Tec-9': 500, 'Desert Eagle': 700}
granadasTR = {'Flash': 200, 'Smoke': 300, 'HE': 300, 'Molotov': 400, 'Distraction': 50}
equipamentosTR = {'Colete e Capacete': 1000, 'Colete': 650, 'ZEUS': 350}
TR = [armasTR, pistolaTR, granadasTR, equipamentosTR]

# CONJUNTO CT
armasCT = {'M4A1': 3100, 'FAMAS': 2100, 'AWP': 4750, 'SSG': 1100, 'MP9': 1250, 'P90': 2100}
pistolaCT = {'USP': 0, 'P250': 300, 'Barretas Duplas': 400, 'Five-Seven': 500, 'Desert Eagle': 700}
granadasCT = {'Flash': 200, 'Smoke': 300, 'HE': 300, 'Incendiary': 600, 'Distraction': 50}
equipamentosCT = {'Colete e Capacete': 1000, 'Colete': 650, 'ZEUS': 350, 'Defuse Kit': 450}
CT = [armasCT, pistolaCT, granadasCT, equipamentosCT]

inventario = []

# ESCOLHA DA EQUIPE
equipe = input('Escolha o seu lado:\nCONTRATERRORISTA \t ou \t TERRORISTA\n\nEscreva aqui sua escolha: ').title()

while equipe != 'Terrorista' and equipe != 'Contraterrorista':
    equipe = input('ESCOLHA INVÁLIDA! Digite novamente: ').title()


if equipe == 'Contraterrorista':
    print('Você é contraterrorista. Escolha seus equipamentos: ')
    while money > 0:
        escolha_de_tipo = int(input('Digite o número do tipo de equipamento:\n1. Armas\n2. Pistola\n'
                                    '3. Granadas\n4. Equipamentos\n5. Sair\n'))
        while escolha_de_tipo <= 0 or escolha_de_tipo > 5:
            print('ESCOLHA INVÁLIDA! Digite novamente:\n')
            escolha_de_tipo = int(input('Digite o número do tipo de equipamento:\n1. Armas\n2. Pistola\n'
                                        '3. Granadas\n4. Equipamentos\n5. Sair\n'))
        if escolha_de_tipo == 5:
            break
        mostrar(CT[escolha_de_tipo-1], money)
        escolha_de_arma = input('Digite o que quer comprar: ').upper()
        ver = verificar(escolha_de_arma, CT[escolha_de_tipo-1])
        while not ver:
            if escolha_de_arma == 'SAIR':
                break
            escolha_de_arma = input('ARMA INCORRETA! Digite novamente\tDigite o que quer comprar: ').upper()
            ver = verificar(escolha_de_arma, CT[escolha_de_tipo-1])
        if escolha_de_arma == 'SAIR':
            break
        money = dinheiro(money, CT[escolha_de_tipo-1][ver[1]])
        inventario.append(ver[1])

if equipe == 'Terrorista':
    print('Você é Terrorista. Escolha seus equipamentos: ')
    while money > 0:
        escolha_de_tipo = int(input('Digite o número do tipo de equipamento:\n1. Armas\n2. Pistola\n'
                                    '3. Granadas\n4. Equipamentos\n5. Sair\n'))
        while escolha_de_tipo <= 0 or escolha_de_tipo > 5:
            print('ESCOLHA INVÁLIDA! Digite novamente:\n')
            escolha_de_tipo = int(input('Digite o número do tipo de equipamento:\n1. Armas\n2. Pistola\n'
                                        '3. Granadas\n4. Equipamentos\n5. Sair\n'))
        if escolha_de_tipo == 5:
            break
        mostrar(TR[escolha_de_tipo-1], money)
        escolha_de_arma = input('Digite o que quer comprar: ').upper()
        ver = verificar(escolha_de_arma, TR[escolha_de_tipo-1])
        while not ver:
            if escolha_de_arma == 'SAIR':
                break
            escolha_de_arma = input('ARMA INCORRETA! Digite novamente\tDigite o que quer comprar: ').upper()
            ver = verificar(escolha_de_arma, TR[escolha_de_tipo-1])
        if escolha_de_arma == 'SAIR':
            break
        money = dinheiro(money, TR[escolha_de_tipo-1][ver[1]])
        inventario.append(ver[1])

print(f'Os itens comprados foram: {Counter(inventario)}')
