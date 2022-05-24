import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#1
# t = np.arange(1, 21, 1)
# print(t)
# plt.plot(t,1/t, label='f(x) = 1/x')
# print()
# plt.xlabel('x')
# plt.ylabel("f(x)")
# plt.title("wykres funkcji f(x) = 1 / x dla x ϵ[1, 20]")
#
# plt.axis([0,max(t),0,1])
# plt.legend()
# plt.show()
#2
# t = np.arange(1, 21, 1)
# print(t)
# plt.plot(t,1/t,'g:>', label='f(x) = 1/x' )
#
# print()
# plt.xlabel('x')
# plt.ylabel("f(x)")
# plt.title("wykres funkcji f(x) = 1 / x dla x ϵ[1, 20]")
#
# plt.axis([0,max(t),0,1])
# plt.legend()
# plt.show()
#3
# x1 = np.arange(0, 31, 0.1)
# x2 = np.arange(0, 31, 0.1)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
# plt.plot(x1, y1, '-')
# plt.plot(x2, y2, 'r-')
# plt.title("sin(x), cos(x)")
# 
# 
# plt.show()
#4
# df = pd.read_csv('iris.csv',header=0,sep=',',decimal='.')
# d = abs(df['sepal length']-df['sepal width'])
# plt.scatter('sepal length', 'sepal width', c=np.random.randn(150), s=d, data=df)
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.show()


#6
df4 = pd.read_csv('zamowienia.csv',header=0,sep=';',decimal='.')
zad4 = df4.groupby(['Sprzedawca']).agg({'Utarg':['sum']})
print(zad4)
myexplode = 9*[0.1]
zad4.plot.pie(subplots=True,autopct='%.2f %%',fontsize=12,figsize=(10,10),shadow='True',explode = myexplode)

plt.show()

#zad1
# x = np.arange(1, 21, 1)
# plt.plot(x, 1/x, label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([0, 20, 0, 1])
# plt.legend()
# plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
# plt.show()
# zad2
# x = np.arange(1, 21, 1)
# plt.plot(x, 1/x, 'g>:', label='f(x) = 1/x' )
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([0, 20, 0, 1])
# plt.legend()
# plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
# plt.show()
# zad3
# x = np.arange(0, 30, .1)
# plt.plot(x, np.sin(x), 'b', label='sin(x)')
# plt.plot(x, np.cos(x), 'r', label='cos(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x) cos(x)')
# plt.legend(loc='upper right')
# plt.title('Wykres sin(x), cos(x)')
# plt.show()

# zad4
# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# print(df)
# # przygotowanie wektora kolorów
# colors = np.random.randint(0, 50, len(df.index))
# # przygotowanie wektora z rozmiarami 'kropek'
# scale = np.abs(df['sepal length'] - df['sepal width'])
#
#
# plt.scatter(df['sepal length'], df['sepal width'], c=colors, s=scale)
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.show()
#zad5
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# plt.subplot(1, 3, 1)
# grouped = df.groupby('Plec')
# etykiety = list(grouped.groups.keys())
# wartosci = list(grouped.agg('Liczba').sum())
# plt.bar(x=etykiety, height=wartosci, color=['green', 'red'])
# plt.xlabel('Płeć')
# plt.ylabel('Liczba narodzonych dzieci')
# # wykres 2
# plt.subplot(1, 3, 2)
# x = df['Rok'].unique()
# kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
# mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
# plt.plot(x, kobiety, label="Kobiety")
# plt.plot(x, mezczyzni, label="Mężczyźni")
# plt.xlabel('Rok')
# #
# # # wykres 3
# plt.subplot(1, 3, 3)
# x = df['Rok'].unique()
# y = df.groupby('Rok').agg('Liczba').sum()
# plt.bar(x, y)
# plt.xlabel('Rok')
# # wyświetlamy cały wykres
# plt.subplots_adjust(wspace=0.85)
# plt.show()
#zad6
df = pd.read_csv('zamowienia.csv', sep=';')
policzone = df.groupby('Sprzedawca')['Utarg'].sum()
print(policzone)
# explode
explode = [0.0 for n in range(len(policzone.index))]
# określamy które kawałki i o ile wysunąć, tu losujemy jeden
explode[np.random.randint(0, len(policzone.index))] = 0.2
wedges, texts, autotext = plt.pie(x=policzone, labels=policzone.index,
                                  autopct=lambda pct: "{:.2f}%".format(pct), textprops=dict(color='black'), explode=explode, shadow=True)
plt.title("Procentowy udział kwot zamówień sprzedawców")
plt.show()
