from math import pow,floor

pocet_radku_sloupcu = 3                            #velikost herni desky 3 - 9
pocet_viteznych_kamenu = 3
symboly = ['X', 'O']                               #symbloly pro hrace 1 a 2


# Uvodni zobrazeni pravidel a nastaveni hry
def uvod() -> None:
    numword = ('', '', '', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    uvod_str = f"""Welcome to Tic Tac Toe
========================================
Game rules:
each player can place one mark (or stone)
per turn on the {pocet_radku_sloupcu} x {pocet_radku_sloupcu} grid. the winner is
who succeeds in placing a sequence of {numword[pocet_radku_sloupcu]} 
of their marks in a:
* horizontal,
* vertical or
* diagonal row
"""
    print(uvod_str)
    nastaveni_hry()
    print("Let's start the game :-)")
    print("--------------------------------------------")


# Dotaz a nastaveni uvodni velikosti hraci plochy a poctu viteznych
# souvislych stejnych symbolu
def nastaveni_hry() -> None:
    global pocet_radku_sloupcu, pocet_viteznych_kamenu
    try:
        pocet_radku_sloupcu = int(input('Set the size of grid n N x N (number between 3 and 9): '))
    except:
        pocet_radku_sloupcu = 3    #default hodnota 3,  pokud nezadano jinak
    try:
        pocet_viteznych_kamenu = int(input('Set the number of winning marks in the sequence (number between 3 and 5): '))
    except:
        pocet_viteznych_kamenu = 3    #default hodnota 3,  pokud nezadano jinak
    print()


# Zobrazeni aktualniho stavu hraci plochy vcetne zobrazeni
# napovedy s cisly poli (cisla tahu)
def hraci_deska(tahy: dict) -> None:
    line = '+---' * pocet_radku_sloupcu + '+'
    print(line,' '*17 + 'Helper')
    for r in tahy:
        radek = '| '
        helper = ' ' * 15
        for s in tahy[r]:
            radek += tahy[r][s] + ' | '
            helper += '{0: <3}'.format(str(r * pocet_radku_sloupcu + s + 1))
        print(radek,helper)
        print(line)

# Ziskani klicu slovniku tahu (radek, sloupec) pro zadany tah cislo
def pozice_tahu(pozice:int) -> list:
    if pozice > int(pow(pocet_radku_sloupcu,2)) or pozice < 1:
        raise
    r = floor(pozice / pocet_radku_sloupcu)
    s = pozice % pocet_radku_sloupcu
    return [r,s-1] if s else [r - 1, pocet_radku_sloupcu - 1]


# Ulozeni znaku hrace to slovniku tahu na pozici zadaneho tahu
def update_tahy(pozice: int, hrac: str, tahy: dict) -> None:
    p = pozice_tahu(pozice)
    tahy[p[0]][p[1]] = hrac


# Vytvoreni sekvenci radku, cloupcu a diagonal podle zadani
# a nasledna kontrola vitesne sekvence
def test_konce_hry(tahy: dict) -> str:
    max_pozice = int(pow(pocet_radku_sloupcu,2))
    #test radku
    for r in range(pocet_radku_sloupcu):
        radek = tahy[r]
        vitez = test_sekvence(''.join(radek.values()))
        if vitez != '':
            return vitez
    #test sloupcu
    for s in range(pocet_radku_sloupcu):
        sequence=''
        for r in range(pocet_radku_sloupcu):
            sequence += tahy[r][s]
            vitez = test_sekvence(sequence)
            if vitez != '':
                return vitez
    #test diagonaly doprava dolu
    for pozice in range(1,max_pozice+1):
        p = pozice_tahu(pozice)
        sequence = tahy[p[0]][p[1]]
        last_pozice = pozice + pocet_radku_sloupcu + 1
        while last_pozice <= max_pozice:
            p = pozice_tahu(last_pozice)
            sequence += tahy[p[0]][p[1]]
            last_pozice += pocet_radku_sloupcu + 1
        if len(sequence) < pocet_viteznych_kamenu:
            continue
        vitez = test_sekvence(sequence)
        if vitez != '':
            return vitez
    #test diagonaly doleva dolu
    for pozice in range(pocet_viteznych_kamenu, max_pozice +1 - (pocet_viteznych_kamenu-1) * pocet_radku_sloupcu):
        p = pozice_tahu(pozice)
        sequence = tahy[p[0]][p[1]]
        last_pozice = pozice + pocet_radku_sloupcu - 1
        while last_pozice <= max_pozice:
            p = pozice_tahu(last_pozice)
            sequence += tahy[p[0]][p[1]]
            last_pozice += pocet_radku_sloupcu - 1
        if len(sequence) < pocet_viteznych_kamenu:
            continue
        vitez = test_sekvence(sequence)
        if vitez != '':
            return vitez
    #zadny z hracu nema pozadovany pocet souvislych kamenu
    return ''


# Kontrola za bylo dosazeno vitezne sekvence n stejnych symbolu
# v predanem radku, sloupci nebo diagonale
def test_sekvence(sequence: str) -> str:
    winpaternX = 'X' * pocet_viteznych_kamenu
    winpaternO = 'O' * pocet_viteznych_kamenu
    if sequence != None and winpaternX in sequence:
        return 'X'
    if sequence != None and winpaternO in sequence:
        return 'O'
    return ''


# Zaverecna zprava pri ukonceni hry viteztvim nebo remizou
# a nasledny dotaz na pokracovani hry
def ukonceni_hry(vitez) -> str:
    if vitez:
        print(f'Congratulations, the player {vitez} WON!')
    else:
        print('Sorry, there is no winner of this game.')
    return input('Enter "Y" for next game or enter for end: ')


# Kontrola zda na zadany tahu (pozici) lze umistit kamen (mark)
# nebo je jiz obsazena
def test_tahu(pozice: int, tahy: dict) -> bool:
    p = pozice_tahu(pozice)
    return True if tahy[p[0]][p[1]] == ' ' else False


# Zadani tahu hrace a kontrola zda je zadani tahu
# (cisla pole) platne a volne
def hrac_tahne(hrac: str, tahy: dict) -> int:
    oddelovac = '=' * 40
    print(oddelovac)
    while True:
        try:
            tah = int(input(f'Player {hrac} | Please enter your move number: '))
            if tah in range(1,int(pow(pocet_radku_sloupcu,2))+1):
                if test_tahu(tah,tahy):
                    break
                else:
                    print('Warning - This position is used.')
                    continue
            else:
                raise
        except:        #spatne zadona pozice kam tahnout (hodnota, typ)
            print(f'Warning - the move has to be a number between 1 to %d !' % (pow(pocet_radku_sloupcu, 2)))
    print(oddelovac)
    return tah

# Pripra a zpusteni nove hry
def nova_hra(tahy: dict) -> None:
    for n in range(1,int(pow(pocet_radku_sloupcu,2))+1):
        update_tahy(n, ' ', tahy)
    print("\n" * 5)
    hraci_deska(tahy)

# Vytvori prazdny slovnik pro umisteni tahu podle zadane velikosti grid
def priprava_hry() -> dict:
   cleartahy = dict()
   for r in range(pocet_radku_sloupcu):        #radek
       cleartahy[r] = dict()
       for s in range(pocet_radku_sloupcu):    #sloupec
          cleartahy[r][s] = ' '
   return cleartahy


def main():
    uvod()
    tahy = priprava_hry()                  #obsahuje jednotlive tahy (obsazeni policek), hodnoty mohou byt 'X','O' nebo ' '
    hraci_deska(tahy)
    toggle = 0
    zbyva_tahu = int(pow(pocet_radku_sloupcu,2))
    while True:
        toggle = toggle ^ 1                #reverze pro stridani hracu
        symbol = symboly[toggle]
        pozice = hrac_tahne(symbol,tahy)
        update_tahy(pozice, symbol, tahy)
        zbyva_tahu -= 1
        hraci_deska(tahy)
        vitez = test_konce_hry(tahy)       #'X','O' nebo kdyz neni vitez False
        if vitez or zbyva_tahu==0:         #pouzity vsechny tahy nebo vitez
            pokracovat = ukonceni_hry(vitez)
            if pokracovat == 'y' or pokracovat == 'Y':
                zbyva_tahu = int(pow(pocet_radku_sloupcu,2))
                nova_hra(tahy)
            else:
                break
    print('Thank you :-)')
    exit()

if __name__ == "__main__":
    main()
