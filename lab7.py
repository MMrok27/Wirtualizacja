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
