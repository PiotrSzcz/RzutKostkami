# IdetycznyRozklad.py
"""Symulowanie 6*x rzutów kostką sześcio boczną do uzyskania identycznej ilości wyrzuconych oczek"""

import time
import random

def pojedynczy_rzut():
    #Liczniki otrzymanych oczek
    pula1 = 0
    pula2 = 0
    pula3 = 0
    pula4 = 0
    pula5 = 0
    pula6 = 0

    for _ in range(1, (6*mnoznik_rzutow)+1):
        wynik_rzutu = random.randrange(1,7)
        if wynik_rzutu == 1:
            pula1 += 1
        elif wynik_rzutu == 2:
            pula2 += 1
        elif wynik_rzutu == 3:
            pula3 += 1
        elif wynik_rzutu == 4:
            pula4 += 1
        elif wynik_rzutu == 5:
            pula5 += 1
        elif wynik_rzutu == 6:
            pula6 += 1

    if pula1 == mnoznik_rzutow and pula2 == mnoznik_rzutow and pula3 == mnoznik_rzutow and pula4 == mnoznik_rzutow and pula5 == mnoznik_rzutow:
        return True
    else:
        return False

mnoznik_rzutow = int(input("Podaj ile razy kazde z oczek ma zostać wyrzucone: "))
licznik_wykonan = 0

czas_poczatek = time.time()

while pojedynczy_rzut() == False:
    pojedynczy_rzut()
    licznik_wykonan += 1

czas_koniec = time.time()

print(f"Czas poczukiwania zdażenia: {czas_koniec-czas_poczatek}s ")
print(f"Petla losujaca wyniki musiała wynonać się: {licznik_wykonan} razy")
input() 
