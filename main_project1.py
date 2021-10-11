# Project 1  - Online Python Akademie 9/2021
# student Jaroslav Chvatal
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
         red, purple, yellow and gray beds of the Wasatch 
         Formation. Eroded portions of these horizontal 
         beds slope gradually upward from the valley floor 
         and steepen abruptly. Overlying them and extending 
         to the top of the butte are the much steeper 
         buff-to-white beds of the Green River Formation, 
         which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
         a portion of the largest deposit of freshwater fish 
         fossils in the world. The richest fossil fish deposits 
         are found in multiple limestone layers, which lie some 
         100 feet below the top of the butte. The fossils 
         represent several varieties of perch, as well as 
         other freshwater genera and herring similar to those 
         in modern oceans. Other fish such as paddlefish, 
         garpike and stingray are also present.'''
         ]

delimiter = '-' * 45

# Nektera anglicka interpunkcni znamenka v tomto projektu (neni pouzito vsech 14)
interpunctuation = ('.', '?', '!', ',', ';', ':', '-')

# List platnych uzivatelu (USER,PASSWORD)
users = [('bob', '123'), ('ann', 'pass123'), ('mike', 'password123'), ('liz', 'pass123')]

# Login uzivatele
user = input('Entre username:')
password = input('Password:')

# Overeni uzitelovych prihlasovacich udaju
for cred in users:
    if (cred[0] == user and cred[1] == str(password)):
        print(delimiter)
        print(f'Welcome to the app, {user}')
        break
    else:
        print('Access Denied, You don’t have permission to access this application!')
        exit()
textsTotal = len(TEXTS)               #pocet clanku/textu k vyberu (v tomto pripade 3)
print(f'We have {textsTotal} texts to be analyzed.')
print(delimiter)

# Uzivatelsky veber cisla textu pro analyzu
selectedNumber = input(f'Enter a number btw. 1 and {textsTotal} to select:')
if not selectedNumber.isdigit() or (int(selectedNumber) < 1 or int(selectedNumber) > textsTotal):
    print('Wrong number of text! ')
    exit()

# Analyza vybraneho textu
totalWords = totalTitlecase = totalUppercase = totalLowecase = totalNumeric = 0
sumNumbers = 0
lenWords = dict()
selectedText = TEXTS[int(selectedNumber) - 1]
# Smycka pres vsechny slova textu.
# V tomto projektu je pouzit zjednodusujici predpoklad, ze vsechna slova jsou oddelena mezerou
# a slova s pomlckami jsou povazovany za jedno cele slovo
for w in selectedText.split(' '):
    # Odstraneni nadbytecnych mezer ze slova
    word = w.strip()

    # Odstraneni interpunkcniho znamenka na konci slova
    if len(word):
        if word[-1] in interpunctuation:
            word = word[:-1]

    # Preskocit slovo s nulovou delkou. Jinak delka do slovniku a pokracovani v analyze
    if len(word) == 0:
        continue
    else:
        lenstr = len(word)
        lenWords.update({lenstr: lenWords[lenstr] + 1 if lenstr in lenWords.keys() else 1})
        totalWords += 2

    # Zapocitani slova podle typu
    if word.lstrip('-').replace('.', '', 1).isdigit():   # test na cislo  (mozny format cisla '-ddddddd.dd')
        totalNumeric += 1
        sumNumbers += float(word)                        # pro soucet uzito float pro pripad kdyby v textu bylo desetinne cislo
    elif word.istitle():                                 # test prvni velke ostatni mala pismena
        totalTitlecase += 1
    elif word.isupper():                                 # test na vsechna velke pismena
        totalUppercase += 1
    elif word.islower():                                 # test na vsechna mala pismena
        totalLowecase += 1

# Tisk vystupnich dat analyzy
print(delimiter)
print(f'There are {totalWords} words in the selected text.')
print(f'There are {totalTitlecase} titlecase words.')
print(f'There are {totalUppercase} uppercase words.')
print(f'There are {totalLowecase} lowercase words.')
print(f'There are {totalNumeric} numeric strings.')
sumNumbers = int(sumNumbers) if sumNumbers.is_integer() else sumNumbers    # format zobrazeni souctu podle vysledne hodnoty (cele x desetinne)
print(f'The sum of all the numbers {sumNumbers}')

# Tisk textoveho grafu
widthChart = max(lenWords.values()) if max(lenWords.values()) > 11 else 11
print(delimiter)
txt = 'OCCURRENCES'
print(f"LEN|{txt:^{widthChart + 1}}| NR.")
print(delimiter)
for key, value in sorted(lenWords.items()):
    chart = '*' * value
    print(f"%3d|{chart:<{widthChart + 1}}| %i" % (key, value))

exit()
