from defs import *


titulo('| BANCO DE DADOS MANUTENÇÃO |')
print('ESCOLHA UMA DAS OPÇÕES A SEGUIR: ')
exp = []
while True:
    while True:
        opc = int(input('\nNovo Registro   [1]: \nRegistro Feitos [2]: \nSair            [3]: \nRESPOSTA:        '))
        linha()
        if 0 < opc <= 4:
            break
    if opc == 1:
        exp.append(new())
    elif opc == 2:
        for i in exp:
            print(i)
        linha()
    else:
        break