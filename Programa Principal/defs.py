def titulo(txt):
    print('=' * len(txt))
    print(f'{txt}')
    print('=' * len(txt))


def linha():
    print('=' * 33)


def new():
    while True:
        lista = []
        vazia = []
        vazia.append(str(input('Máquina: ')))
        vazia.append(int(input('Número da máquina: ')))
        lista.append(vazia[:])
        vazia.clear()
        linha()
        while True:
            r = str(input('Quer Adicionar Mais: [s/n] ')).strip().upper()
            linha()
            if r in 'SN':
                break
        if r == 'N':
            break
    return lista