from pakiet import *

napis = 'amogus'
lit.wyswietl(napis)

print(lit.dlugosc(napis))
print(dod.dzialanie(1,2))

plik = open('tekst.txt', 'r')
znaki = plik.read(10)
linia = plik.readline()
wiersze = plik.readlines()

plik.close()
print(znaki)
print(linia)
print(wiersze)

import sys
print('Podaj kierunek, rok i specjalizacje')
dane = sys.stdin.readline()

plik = open('dane.txt', 'w+')
plik.write(dane)
plik.close()
lista = []
for i in range(0,11):
    lista.append(i)
plik = open('dane.txt', 'a+')
plik.writelines(str(lista))
plik.close()

with open('tekst.txt', 'r') as plik:
    for linia in plik:
        print(linia, end='')

class PierwszaKlasa:
    """"pierwsza klasa python"""
    atrybut = 69420
    def pierwsza_metoda(self):
        return 'amogus'

obiekt = PierwszaKlasa()
print(obiekt)
print(obiekt.atrybut)
obiekt.tekst = 'napisus'
print(obiekt.tekst)
# obiekt2 = PierwszaKlasa()
# print(obiekt2.tekst)
print(obiekt.pierwsza_metoda())

class Ksztalty:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opis = 'To bd klasa dla ogólnych kształtów'

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2*self.x + 2*self.y

    def dod_opis(self, text):
        self.opis = text

    def skalowanie(self,czyn):
        self.x = self.x * czyn
        self.y = self.y * czyn

prostakat = Ksztalty(10, 30)
print(prostakat.pole())
print(prostakat.obwod())
print(prostakat.opis)
prostakat.dod_opis('prostokąt')
print(prostakat.opis)
prostakat.skalowanie(0.5)
print(prostakat.x)
print(prostakat.y)
