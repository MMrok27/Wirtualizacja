import numpy as np
#1
a= np.array([2,9,7,9])
b= np.array([5,6,4,7])
c1=a*b
print(c1)
#2
c = np.arange(9)
c = c.reshape((3,3))
d = np.arange(16)
d = d.reshape((4,4))
print(c)
print(np.min(c,axis=0))
print(np.min(c,axis=1))
print(d)
print(np.min(d,axis=0))
print(np.min(d,axis=1))
#3
print(a.dot(b))
#4
a2= np.array([6,9,4])
b2= np.array([1.2,6.4,2.2])
c2=a2*b2
print(c2)
#5
ar = np.arange(6)
br = ar.reshape((2,3))
a = np.sin(br)
print(a)
#6
cr = np.arange(6)
dr = cr.reshape((2,3))
b = np.cos(dr)
print(b)
#7
print(a+b)
#8
a = np.arange(9).reshape((3,3))
for b in a:
    print(b)
#9
a = np.arange(9).reshape((3,3))
for b in a.flat:
    print(b)
#10
nxn = np.arange(81).reshape((9,9))
print(nxn)
nxn2 = nxn.reshape((3,27))
print(nxn2)
nxn3 = nxn.reshape((27,3))
print(nxn3)
#11
pl = np.arange(12)
print(pl)
pl2 = pl.reshape(3,4)
pl3 = pl.reshape(4,3)
pl4 = pl.reshape(2,6)
print(pl2)
print(pl3)
print(pl4)
for b in pl2.flat:
    print(b)

for b in pl3.flat:
    print(b)

for b in pl4.flat:
    print(b)


#Zad1
# a = np.array([3, 4, 5])
# b = np.array([6, 2, 4])
# c = a * b
# print(c)

#Zad2
# a = np.array([[3, 7, 5], [6, 1, 9], [2, 7, 8]])
# b = np.array([[5, 1, 6, 8], [3, 6, 2, 7], [9, 3, 7, 5], [4, 4, 2, 1]])
# print(a)
# print(b)
#
# print(a.min(axis=0))
# print(a.min(axis=1))
# print(b.min(axis=0))
# print(a.min(axis=1))

#Zad3
# a = np.array([3, 4, 5])
# b = np.array([6, 2, 4])
# c = np.dot(a, b)
# print(c)

#Zad4
# a = np.array([3, 4, 5])
# b = np.linspace(3, 10, 3)
# c = a * b
# print(c)

#Zad5,6,7
# c = np.array([[60, 31], [45, 78], [15, 50]])
# a = np.sin(c)
# print(a)
#
#
# d = np.array([[47, 24], [64, 28], [19, 33]])
# b = np.cos(d)
# print(b)
# print("")
# dodawanie = np.add(a,b)
# print(dodawanie)

#Zad8
# a = np.array([[3, 7, 5], [6, 1, 9], [2, 7, 8]])
# for b in a:
#     print(b)
#     print("")

#Zad9
# a = np.array([[3, 7, 5], [6, 1, 9], [2, 7, 8]])
# for b in a.flat:
#     print(b)
#     print("")

#Zad10
# macierz = np.arange(0,81,1).reshape(9,9)
# print(macierz)
#
# macierz_1 = macierz.reshape(3,27)
# print(macierz_1)
# macierz_2 = macierz.reshape(27,3)
# print(macierz_2)
# macierz_3 = macierz.reshape(81,1)
# print(macierz_3)
# macierz_4 = macierz.ravel()
# print(macierz_4)

#Zad11
a = np.array([3, 7, 5, 6, 1, 9, 2, 7, 8, 6, 3, 6])
print(a)
macierz_1 = a.reshape(3, 4)
print(macierz_1)
print(macierz_1.ravel())
macierz_2 = macierz_1.reshape(4,3)
print(macierz_2)
print(macierz_2.ravel())
macierz_3 = macierz_1.reshape(2,6)
print(macierz_3)
print(macierz_3.ravel())
