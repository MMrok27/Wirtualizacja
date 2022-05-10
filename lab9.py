import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,header=0)

nic = df.groupby(['Rok']).agg({'Liczba':['sum']})
print(nic)
unik = df['Rok'].unique()

nic.plot()
plt.xticks(unik, rotation=90)
plt.show()

plec = df.groupby(['Plec']).agg({'Liczba':['sum']})
print(plec)

plec.plot(kind='bar',xlabel='Płeć',ylabel='Liczba urodzeń (w milionach)',rot=0, title='Liczba urodzonych chłopców i dziewczynek z całego zbioru')
plt.legend(['Wartości'])
plt.show()

df2=df[(df.Rok > 2012)]
plec2 = df2.groupby(['Plec']).agg({'Liczba':['sum']})
print(plec2)
plec2.plot.pie(subplots=True,autopct='%.2f %%',fontsize=10,figsize=(6,6),legend=(0,0))
plt.show()

df4 = pd.read_csv('zamowienia.csv',header=0,sep=';',decimal='.')
zad4 = df4.groupby(['Sprzedawca']).agg({'Utarg':['count']})

zad4.plot(kind='bar',xlabel='Nazwa',ylabel='Liczba zamówień',rot=0, title='Liczba zamówień przez sprzedawców')
plt.legend(['Wartości'])
plt.show()
