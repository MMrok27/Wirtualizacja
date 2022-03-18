######################ZAD 1################################
import random

lista = [1-x for x in range(1, 11)]
print(lista)

listb = [4**x for x in range(0, 6)]
print(listb)

listc = [x for x in listb if x % 2 == 0]
print(listc)

######################ZAD 2################################



list1 = [random.randint(1, 100) for x in range(0, 10)]
print(list1)

list2 = [x for x in list1 if x % 2 == 0]
print(list2)

######################ZAD 3################################
zakupy = {"mleko": 'szt', "jabłko": 'szt', 'woda': 'l'}
print(zakupy)
list3 = [key for key, value in zakupy.items() if value == 'szt']
print(list3)
######################ZAD 4################################
def prostok(a,b,c):
    if a**2 + b**2 == c**2:
        return 'prostokatny'
    else: return 'nie prostokatny'
print(prostok(3,4,5))
######################ZAD 5################################
def ptrapez(a=1,b=1,h=1):
    return ((a+b)*h)/2
print(ptrapez(3,4,5))
print(ptrapez(2))
######################ZAD 6################################
def ciag(a=1,b=4,ile=10):
    iloczyn=a
    for x in range(1,ile):
        iloczyn=iloczyn*b*x*a
    return iloczyn
print(ciag(2,2,3))
######################ZAD 7################################

def ciag2(*liczby):
    iloczyn = 1
    for x in liczby:
        iloczyn = iloczyn * x
    return iloczyn

print(ciag2(2,5,6))
######################ZAD 8################################

def wart(** rzeczy):
    cw=0
    il=0
    for cos in rzeczy:
        cw=cw+rzeczy[cos]
        il=il+1
    print("jest tyle produktów:",il)
    return cw


print(wart(mleko = 5, jabłko= 2, woda= 3))
######################ZAD 9################################
from ciagi import *
print(aryt.suman(1,2,2))
print(aryt.nwyraz(1,2,2))

print(geo.suman(1,2,2))
print(geo.nwyraz(1,2,2))