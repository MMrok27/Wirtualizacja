import numpy as np
import pandas as pd
#1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,header=0)
print(df)
#2
print(df[df['Liczba']>1000])
print(df[df['Imie']=='MICHAŁ'])
print(df.agg({'Liczba':['sum']}))

print(df[((df.Rok > 1999) & (df.Rok < 2006))].agg({'Liczba':['sum']}))
print(df.groupby(['Plec']).agg({'Liczba':['sum']}))

nic = (df.sort_values('Liczba', ascending = False).groupby(['Rok','Plec']).first())
print(nic)

nid = df[df['Plec'] == 'K'].groupby('Imie')[["Liczba"]].sum().sort_values('Liczba', ascending = False)[:1]
nic = df[df['Plec'] == 'M'].groupby('Imie')[["Liczba"]].sum().sort_values('Liczba', ascending = False)[:1]
print(nid)
print(nic)
#3
df2 = pd.read_csv('zamowienia.csv',header=0,sep=';',decimal='.')
print(df2)

unik = df2['Sprzedawca'].unique()
print(unik)
print(df2.sort_values('Utarg', ascending = False).head(5))

print(df2.groupby(['Sprzedawca']).size().reset_index(name='ile'))

print(df2.groupby(['Kraj'])[["Utarg"]].sum())
df2['Data zamowienia'] = pd.to_datetime(df2['Data zamowienia'])
print(df2[((df2['Kraj']=='Polska') & (pd.DatetimeIndex(df2['Data zamowienia']).year == 2005))].agg({'Utarg':['sum']}))

print(df2[(pd.DatetimeIndex(df2['Data zamowienia']).year == 2004)]['Utarg'].mean(axis=0))

df3=df2[(pd.DatetimeIndex(df2['Data zamowienia']).year == 2004)]

df4=df2[(pd.DatetimeIndex(df2['Data zamowienia']).year == 2005)]

df3.to_csv('zamówienia_2004.csv',index=False)

df4.to_csv('zamówienia_2005.csv',index=False)



