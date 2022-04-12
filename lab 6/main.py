import numpy as np
#1
a = 4 ** np.arange(1,21)
print(a)
#2
b = np.arange(1,10.5,0.5)
print(b)
c = b.astype('int32')
print(c)
#3
def zad3(n):
    tab=(2**np.arange(1,(n**2)+1)).reshape(n,n)
    return tab
print(zad3(2))
#4
def zad4(n,m):
    tab=np.logspace(1,m,num=m,base=n)
    return tab
print(zad4(3,6))
#5

#6


#7
#8
#9