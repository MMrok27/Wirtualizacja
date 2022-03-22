######################ZAD 1################################


lista = [x * 2 for x in range(0, 31)]
plik = open('dane.txt', 'w+')
plik.writelines(str(lista))
plik.close()

######################ZAD 2################################
plik = open('dane.txt', 'r')
dane = plik.readlines()
print(dane)
plik.close()

######################ZAD 3################################
import sys
with open('tekst.txt', 'w+') as plik:
    for x in range(1,3):
        linia = sys.stdin.readline()
        plik.write(linia)

with open('tekst.txt', 'r') as plik:
     for linia in plik:
         print(linia, end='')

######################ZAD 4################################
class NaZakupy:
    def __init__(self, x, y,z,zz):
        self.nazwa_produktu=x
        self.ilosc=y
        self.jednostka_miary=z
        self.cena_jed=zz
    def wyswietl_produkt(self):
        print("nazwa produktu: "+ self.nazwa_produktu)
        print("ilość: " + str(self.ilosc))
        print("jednostka: " + self.jednostka_miary)
        print("cena: " + str(self.cena_jed))
    def ile_produktu(self):
        print("ilość: " + str(self.ilosc) +" "+ self.jednostka_miary)
    def ile_kosztuje(self):
        print(self.ilosc * self.cena_jed)
chleb = NaZakupy('chleb',3,'szt',4)
chleb.wyswietl_produkt()
chleb.ile_produktu()
chleb.ile_kosztuje()

######################ZAD 5################################
class CiagA:
    def __init__(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
        self.ciag = [a1 + r * x for x in range(0, n)]

    def pobierz_element(self, index):
        if index > self.n - 1 or index < 0:
            print('Zły index')
            return -1
        return self.ciag[index]

    def pobierz_parametry(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
        self.ciag = [a1 + r * x for x in range(0, n)]

    def policz_sume(self):
        suma = 0
        for x in range(0, self.n):
            suma += self.ciag[x]
        return suma

    def ile_elementuw(self):
        return self.n


ciag = CiagA(0, 2, 10)
print(ciag.ciag)
print(ciag.pobierz_element(9))
ciag.pobierz_parametry(0, 2, 10)
print(ciag.ciag)
print(ciag.policz_sume())
print(ciag.ile_elementuw())
######################ZAD 6################################
class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_n(self, ile):
        self.y += ile * self.krok

    def idz_e(self, ile):
        self.x += ile * self.krok

    def idz_s(self, ile):
        self.y -= ile * self.krok

    def idz_w(self, ile):
        self.x -= ile * self.krok

    def gdzie_jestes(self):
        print('x: ' + str(self.x) + ', y: ' + str(self.y))


mujrobaczek = Robaczek(6, 9, 1)
mujrobaczek.gdzie_jestes()
mujrobaczek.idz_n(6)
mujrobaczek.gdzie_jestes()
mujrobaczek.idz_e(9)
mujrobaczek.gdzie_jestes()
mujrobaczek.idz_s(4)
mujrobaczek.gdzie_jestes()
mujrobaczek.idz_w(20)
mujrobaczek.gdzie_jestes()
