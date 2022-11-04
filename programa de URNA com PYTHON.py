import os
bolsonaro = 0
lula = 0

while True:

    print('*'*20)
    print(f'total Bolsonaro:{bolsonaro}{os.linesep}total Lula:{lula}')
    print('*'*20)
    try:
        voto = int(input(f'seu voto{os.linesep}22 - Bolsonaro{os.linesep}13 - lula{os.linesep}seu voto: '))
        if voto == 22:
            bolsonaro += 1
        elif voto == 13:
            lula += 1
        else:
            pass

    except:
         print('vote 13 ou 22')
    os.system('cls')


