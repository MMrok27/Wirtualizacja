# zad 1
import sys as system
import math
sporty = ["piłka nożna", "siatkówka"]
sporty.reverse()
sporty.append("koszykówka")
print(sporty)
# zad 2
slownik = {"brb": "be right back", "etc": "et cetera"}
print(slownik)
# zad 3
gry = {"MGR:R": "Metal Gear Rising: Revengeance", "MC": "Minecraft", "Ter": "Terraria", "S;G": "Steins;Gate"}
print(gry)
print(len(gry.keys()))
# zad 4
napis = input("podaj napis: ")
a = napis.count("a")
print("Liter a jest:", a)
# zad 5
system.stdout.write("Podaj 3 liczby: ")
l1 = system.stdin.readline()
l2 = system.stdin.readline()
l3 = system.stdin.readline()
l1 = int(l1)
l2 = int(l2)
l3 = int(l3)

wynik = l1 ** l2 + l3
wynik = str(wynik)
system.stdout.write(wynik)
system.stdout.write("\n")

# zad 6
l1 = input("podaj liczbe 1: ")
l2 = input("podaj liczbe 2: ")
l3 = input("podaj liczbe 3: ")
l1 = int(l1)
l2 = int(l2)
l3 = int(l3)

if l1 > l2:
    if l1 > l3:
        print(l1)
    elif l3 > l1:
        print(l3)
    else:
        print("l1 i l3 sa takie same = ", l1)
elif l2 > l1:
    if l2 > l3:
        print(l2)
    elif l3 > l2:
        print(l3)
    else:
        print("l2 i l3 sa takie same = ", l2)
elif l1 == l2 == l3:
    print("l1, l2 i l3 sa takie same = ", l1)
else:
    print("l1 i l2 sa takie same = ", l1)

# zad 7
lista = [3.2, 2, 22, 4.20, 6.9, 13]
lista2 = [x ** 2 for x in lista]
print(lista2)
# zad 8
tab = []
i = 0
while i != 10:
    licz = input("podaj liczbe: ")
    licz = int(licz)
    if licz % 2 == 0:
        tab.append(licz)
    i += 1
print(tab)
# zad 9
l1 = input("podaj liczbe: ")
l1 = int(l1)

try:
    print(math.sqrt(l1))
except ValueError:
    print("Liczba musi byc większa od 0")
