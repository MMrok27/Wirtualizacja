# zad1
import math

a = "amogus"
b = "sus"
c = 2
d = 69
de = 5.7
f = -4.2
g = 7 + 3j
h = 8 + 10j
print(a, b, c, d, de, f, g, h)
# zad2
l1 = input("podaj l1: ")
l2 = input("podaj l2: ")
l1 = float(l1)
l2 = float(l2)
print('%(z1)f+%(z2)f=%(z3)f' % {'z1': l1, 'z2': l2, 'z3': l1 + l2})
print('%(z1)f-%(z2)f=%(z3)f' % {'z1': l1, 'z2': l2, 'z3': l1 - l2})
print('%(z1)f*%(z2)f=%(z3)f' % {'z1': l1, 'z2': l2, 'z3': l1 * l2})
print('%(z1)f/%(z2)f=%(z3)f' % {'z1': l1, 'z2': l2, 'z3': l1 / l2})
# zad3
a = 34
b = 15
f += 1
b -= 1
c *= 2
d /= 3
de **= 2
a %= 2
print(a, b, c, d, de, f)
# zad4

print(math.e ** 10)
sinus = math.sin(8) ** 2
wynik = (math.log(5) + sinus) ** (1 / 6)
print(wynik)

print(math.floor(3.55))
print(math.ceil(4.80))

# zad5
imie = "MICHAL"
nazwisko = "MROCZEK"
imie = str.capitalize(imie)
nazwisko = str.capitalize(nazwisko)
print(imie, nazwisko)
# zad6
slowa = "la la la la le"
print(slowa.count("la"))
# zad7
slowo = "amogus"
print(slowo[1], slowo[len(slowo) - 1])
# zad8
print(slowa.split())

# zad9
a = "string"
b = 34.76
c = 0x01234567

print(a, b, hex(c))
