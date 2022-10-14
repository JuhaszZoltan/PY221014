print('''
=====árlista=====
alma    599 Ft/Kg
szőlő  1398 Ft/Kg
szilva  499 Ft/Kg
''')
vegosszeg:int = 0
kerdes = 'Jó napot kívánok!\nSzeretne valamit vásárolni? '
while input(kerdes) == 'igen':
    termek = input('mit szeretnél vásárolni? ')
    if termek not in ['alma', 'szilva', 'szőlő']:
        print(f'Sajnos {termek}t nem árulunk :(')
    else:
        reszosszeg:int = 0
        mennyiseg:float = float(input(f'Hány kiló {termek}t szeretnél vásárolni? '))
        if termek == 'alma':
            reszosszeg = mennyiseg * 599
        elif termek == 'szilva':
            reszosszeg = mennyiseg * 499
        else:
            reszosszeg = mennyiseg * 1398
        print(f'Ez {reszosszeg} Ft lesz.')
        vegosszeg += reszosszeg
    kerdes = 'Szerene még valamit vásárolni? '
print(f'rendben, összesen {vegosszeg} Ft-ot kérek!')
print('viszont látásra!')