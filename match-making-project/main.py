from random import randint

# COMPETIDORES
comp = []
qntd = int(input('Quantos jogadores serão? '))

for x in range(1, qntd+1):
    jogador = input(f'Insira o nome do jogador {x}: ')
    comp.append(jogador)

print(comp)

# SORTEIO
for x in range(1, int(len(comp)/2)+1):
    y = randint(0, len(comp)-1)

    z = randint(0, len(comp)-1)
    while z == y:
        z = randint(1, len(comp)-1)

    a = comp[y]
    b = comp[z]

    comp.remove(a)
    comp.remove(b)

    print(f"O duelo {x} será: {a} x {b}")

if len(comp) == 1:
    print(f'\nO jogador que sobrou foi: {comp[0]}')