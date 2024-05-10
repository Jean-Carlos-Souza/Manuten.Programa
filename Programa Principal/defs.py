def titulo(txt):
    print('=' * len(txt))
    print(f'{txt}')
    print('=' * len(txt))


def linha():
    print('=' * 33)


def new():
    while True:
        vazia = list.clear
        lista = list
        vazia = str(input('Nome da Máquina: '))
        vazia = str(input('Setor da Máquina: '))
        lista = vazia
        while True:
            r = str(input('Quer Adicionar Mais: [s/n]')).strip().upper()
            if r in 'SN':
                break
        if r == 'N':
            break
    print(lista)
    return lista