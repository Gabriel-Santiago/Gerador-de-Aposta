import numpy as np


def loop():
    choose = input('''Deseja Jogar de novo?
    Y - Yes
    N - No
    :''')

    if choose == 'Y' or choose == 'y':
        sorteio()
    elif choose == 'N' or choose == 'n':
        print('Bye! :(')
    else:
        print('Tecla inválida')
        loop()


def sorteio_quina():
    try:
        numbers = int(input(f'Bem vindo a Quina!\n'
                f'Digite quantos números vão ser escolhidos: '))
    except ValueError:
        print('ERRO: Apenas número', end='\n')
        sorteio_quina()
    else:
        quina = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
        if 4 < numbers < 16:
            match numbers:
                case 5:
                    quinaSorte = np.random.choice(quina, numbers, False)
                    sorte = str(quinaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 1,50')
                    loop()
                case 6:
                    quinaSorte = np.random.choice(quina, numbers, False)
                    sorte = str(quinaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 9,00')
                    loop()
                case 7:
                    quinaSorte = np.random.choice(quina, numbers, False)
                    sorte = str(quinaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 31,50')
                    loop()
                case 8:
                    quinaSorte = np.random.choice(quina, numbers, False)
                    sorte = str(quinaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 84,00')
                    loop()
                case 9:
                    quinaSorte = np.random.choice(quina, numbers, False)
                    sorte = str(quinaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 189,00')
                    loop()
                case 10:
                    quinaSorte = np.random.choice(quina, numbers, False)
                    sorte = str(quinaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 378,00')
                    loop()
                case 11:
                    quinaSorte = np.random.choice(quina, numbers, False)
                    sorte = str(quinaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 693,00')
                    loop()
                case 12:
                    quinaSorte = np.random.choice(quina, numbers, False)
                    sorte = str(quinaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 1188,00')
                    loop()
                case 13:
                    quinaSorte = np.random.choice(quina, numbers, False)
                    sorte = str(quinaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 1930,50')
                    loop()
                case 14:
                    quinaSorte = np.random.choice(quina, numbers, False)
                    sorte = str(quinaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 3003,00')
                    loop()
                case 15:
                    quinaSorte = np.random.choice(quina, numbers, False)
                    sorte = str(quinaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 4504,50')
                    loop()
        else:
            print('Na Quina você pode escolher somente entre 5 e 15 números!')
            sorteio_quina()


def sorteio_lotomania():
    lotomania = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

    print(f'Bem vindo a Lotomania!\n'
          f'Serão sorteado os 50 números para você ganhar!')

    lotomaniaSorte = np.random.choice(lotomania, 50, False)
    sorte = str(lotomaniaSorte)[1:-1]
    print(f'Os números para você ganhar são: \n{sorte}\n'
          f'O valor da aposta é R$ 1,50')
    loop()


def sorteio_lotofacil():
    try:
        numbers = int(input(f'Bem vindo a Lotofácil!\n'
                            f'Digite quantos números vão ser escolhidos: '))
    except ValueError:
        print('ERRO: Apenas número', end='\n')
        sorteio_lotofacil()
    else:
        lotofacil = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        if 14 < numbers < 19:
            match numbers:
                case 15:
                    lotofacilSorte = np.random.choice(lotofacil, numbers, False)
                    sorte = str(lotofacilSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 2,00')
                    loop()
                case 16:
                    lotofacilSorte = np.random.choice(lotofacil, numbers, False)
                    sorte = str(lotofacilSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 32,00')
                    loop()
                case 17:
                    lotofacilSorte = np.random.choice(lotofacil, numbers, False)
                    sorte = str(lotofacilSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 272,00')
                    loop()
                case 18:
                    lotofacilSorte = np.random.choice(lotofacil, numbers, False)
                    sorte = str(lotofacilSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 1632,00')
                    loop()
        else:
            print('Na Lotofácil você pode escolher somente entre 15 e 18 números!')
            sorteio_lotofacil()


def sorteio_diaSorte():
    try:
        numbers = int(input(f'Bem vindo ao Dia de Sorte!\n'
                            f'Digite quantos números vão ser escolhidos: '))
    except ValueError:
        print('ERRO: Apenas número', end='\n')
        sorteio_diaSorte()
    else:
        dia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29, 30, 31]
        mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
               'novembro', 'dezembro']
        if 6 < numbers < 16:
            match numbers:
                case 7:
                    diaSorte = np.random.choice(dia, numbers, False)
                    mesSorte = np.random.choice(mes, 1, False)
                    sorte = str(diaSorte)[1:-1]
                    sorte2 = str(mesSorte)[1:-1]
                    print(f'O mês da sorte é {sorte2}\n'
                          f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 2,00')
                    loop()
                case 8:
                    diaSorte = np.random.choice(dia, numbers, False)
                    mesSorte = np.random.choice(mes, 1, False)
                    sorte = str(diaSorte)[1:-1]
                    sorte2 = str(mesSorte)[1:-1]
                    print(f'O mês da sorte é {sorte2}\n'
                          f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 16,00')
                    loop()
                case 9:
                    diaSorte = np.random.choice(dia, numbers, False)
                    mesSorte = np.random.choice(mes, 1, False)
                    sorte = str(diaSorte)[1:-1]
                    sorte2 = str(mesSorte)[1:-1]
                    print(f'O mês da sorte é {sorte2}\n'
                          f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 72,00')
                    loop()
                case 10:
                    diaSorte = np.random.choice(dia, numbers, False)
                    mesSorte = np.random.choice(mes, 1, False)
                    sorte = str(diaSorte)[1:-1]
                    sorte2 = str(mesSorte)[1:-1]
                    print(f'O mês da sorte é {sorte2}\n'
                          f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 240,00')
                    loop()
                case 11:
                    diaSorte = np.random.choice(dia, numbers, False)
                    mesSorte = np.random.choice(mes, 1, False)
                    sorte = str(diaSorte)[1:-1]
                    sorte2 = str(mesSorte)[1:-1]
                    print(f'O mês da sorte é {sorte2}\n'
                          f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 660,00')
                    loop()
                case 12:
                    diaSorte = np.random.choice(dia, numbers, False)
                    mesSorte = np.random.choice(mes, 1, False)
                    sorte = str(diaSorte)[1:-1]
                    sorte2 = str(mesSorte)[1:-1]
                    print(f'O mês da sorte é {sorte2}\n'
                          f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 1584,00')
                    loop()
                case 13:
                    diaSorte = np.random.choice(dia, numbers, False)
                    mesSorte = np.random.choice(mes, 1, False)
                    sorte = str(diaSorte)[1:-1]
                    sorte2 = str(mesSorte)[1:-1]
                    print(f'O mês da sorte é {sorte2}\n'
                          f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 3432,00')
                    loop()
                case 14:
                    diaSorte = np.random.choice(dia, numbers, False)
                    mesSorte = np.random.choice(mes, 1, False)
                    sorte = str(diaSorte)[1:-1]
                    sorte2 = str(mesSorte)[1:-1]
                    print(f'O mês da sorte é {sorte2}\n'
                          f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 6864,00')
                    loop()
                case 15:
                    diaSorte = np.random.choice(dia, numbers, False)
                    mesSorte = np.random.choice(mes, 1, False)
                    sorte = str(diaSorte)[1:-1]
                    sorte2 = str(mesSorte)[1:-1]
                    print(f'O mês da sorte é {sorte2}\n'
                          f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 12870,00')
                    loop()
        else:
            print('No Dia da Sorte você pode escolher somente entre 7 e 15 números!')
            sorteio_diaSorte()


def sorteio_megaSena():
    try:
        numbers = int(input(f'Bem vindo a Mega Sena!\n'
                            f'Digite quantos números vão ser escolhidos: '))
    except ValueError:
        print('ERRO: Apenas número', end='\n')
        sorteio_megaSena()
    else:
        megaSena = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                    28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                    53,
                    54, 55, 56, 57, 58, 59, 60]
        if 5 < numbers < 16:
            match numbers:
                case 6:
                    megaSenaSorte = np.random.choice(megaSena, numbers, False)
                    sorte = str(megaSenaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 3,50')
                    loop()
                case 7:
                    megaSenaSorte = np.random.choice(megaSena, numbers, False)
                    sorte = str(megaSenaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 24,50')
                    loop()
                case 8:
                    megaSenaSorte = np.random.choice(megaSena, numbers, False)
                    sorte = str(megaSenaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 98,00')
                    loop()
                case 9:
                    megaSenaSorte = np.random.choice(megaSena, numbers, False)
                    sorte = str(megaSenaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 294,00')
                    loop()
                case 10:
                    megaSenaSorte = np.random.choice(megaSena, numbers, False)
                    sorte = str(megaSenaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 735,00')
                    loop()
                case 11:
                    megaSenaSorte = np.random.choice(megaSena, numbers, False)
                    sorte = str(megaSenaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 1617,00')
                    loop()
                case 12:
                    megaSenaSorte = np.random.choice(megaSena, numbers, False)
                    sorte = str(megaSenaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 3234,00')
                    loop()
                case 13:
                    megaSenaSorte = np.random.choice(megaSena, numbers, False)
                    sorte = str(megaSenaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 6006,00')
                    loop()
                case 14:
                    megaSenaSorte = np.random.choice(megaSena, numbers, False)
                    sorte = str(megaSenaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 10510,50')
                    loop()
                case 15:
                    megaSenaSorte = np.random.choice(megaSena, numbers, False)
                    sorte = str(megaSenaSorte)[1:-1]
                    print(f'Os números para você ganhar são: \n{sorte}\n'
                          f'O valor da aposta é R$ 17517,50')
                    loop()
        else:
            print('Na Mega Sena você pode escolher somente entre 6 e 15 números!')
            sorteio_megaSena()


def sorteio():
    try:
        choice = int(input('''Deseja ganhar uma bolada??
            Então escolha uma das opções abaixo e te mostraremos o resultado
            1 - Quina
            2 - Lotomania
            3 - Lotofácil
            4 - Dia de Sorte
            5 - Mega Sena
            :'''))
    except ValueError:
        print('ERRO: Apenas número', end='\n')
        sorteio()
    else:
        match choice:
            case 1:
                sorteio_quina()
            case 2:
                sorteio_lotomania()
            case 3:
                sorteio_lotofacil()
            case 4:
                sorteio_diaSorte()
            case 5:
                sorteio_megaSena()
            case _:
                print('Número inválido!')
                loop()


def main():
    sorteio()


main()
