# FUNÇÃO PARA SEPARAR PARTE INTEIRA E FRACIONÁRIA
def separar(c):
    h = str(c)
    y = h.split(".")
    a = int(y[0])
    b = float("0." + y[1])
    if b != 0:
        return a, b
    else:
        return a, 0


# VARIÁVEIS PARA RESPOSTA
binario = []
bindec = []

# ENTRADA DE DADOS
n = float(input("Digite o número em decimal: "))

# TRATAMENTO DOS DADOS
n = separar(n)
num = n[0]
dec = n[1]

# ENTRADA DE DADOS PARA A QUANTIDADE DE CASAS DECIMAIS
if dec != 0:
    repeticoes = int(input("Com quantas casas decimais você quer aproximar? "))

# CONVERSÃO DA PARTE INTEIRA DO DECIMAL PARA BINÁRIO
while num >= 2:
    binario.append(num % 2)
    num = int(num/2)

binario.append(num)

# CONVERSÃO DA PARTE FRACIONÁRIA DO DECIMAL PARA BINÁRIO
if dec != 0:
    bindec.append(',')
    for x in range(0, repeticoes):
        dec = dec*2
        if dec >= 1:
            bindec.append('1')
            dec = dec - 1
        else:
            bindec.append('0')

# AMOSTRAGEM DOS RESULTADOS
print("O resultado em binário é: ", end="", flush=True)
for x in reversed(binario):
    print(x, end="", flush=True)

for x in bindec:
    print(x, end="", flush=True)

# OCTAL
# DECLARAÇÃO DE VARIAVEIS
octal = []
octaldec = []

num = n[0]
dec = n[1]

# CONVERSÃO DA PARTE INTEIRA DO DECIMAL PARA OCTAL
while num >= 8:
    octal.append(num % 8)
    num = int(num/8)

octal.append(num)

# CONVERSÃO DA PARTE FRACIONÁRIA DO DECIMAL PARA BINÁRIO
if dec != 0:
    octaldec.append(',')
    for x in range(0, repeticoes):
        dec = dec*8
        z = int(dec)
        octaldec.append(z)
        dec = dec - z

# AMOSTRAGEM DOS RESULTADOS
print("\nO resultado em octal é: ", end="", flush=True)
for x in reversed(octal):
    print(x, end="", flush=True)

for x in octaldec:
    print(x, end="", flush=True)

# HEXADECIMAL
# DECLARAÇÃO DE VARIAVEIS
hexa = []
hexadec = []
vhexa = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

num = n[0]
dec = n[1]

# CONVERSÃO DA PARTE INTEIRA DO DECIMAL PARA OCTAL
while num >= 16:
    hexa.append(vhexa[num % 16])
    num = int(num/16)

hexa.append(num)

# CONVERSÃO DA PARTE FRACIONÁRIA DO DECIMAL PARA BINÁRIO
if dec != 0:
    hexadec.append(',')
    for x in range(0, repeticoes):
        dec = dec*16
        z = int(dec)
        hexadec.append(vhexa[z])
        dec = dec - z

# AMOSTRAGEM DOS RESULTADOS
print("\nO resultado em hexadecimal é: ", end="", flush=True)
for x in reversed(hexa):
    print(x, end="", flush=True)

for x in hexadec:
    print(x, end="", flush=True)
