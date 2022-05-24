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


#zad1,2
# plik = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(plik, header=0)
#
# print(df[df.Liczba > 1000])
# print('')
# print(df[df.Imie == 'RADOSŁAW'])
# print('')
# print(df.Liczba.sum())
# print('')
# grupa = df[df.Rok < 2006]
# print(grupa.Liczba.sum())
# grupa = df[df.Rok < 2006].groupby('Rok').agg({'Liczba': ['sum']})
# print(grupa)
# print('')
#
# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))
# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())
#
# new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
# for index, group in enumerate(new_df, start=1):
#     print(f"{index} {group[0]}")
#     print(f" {group[1].iloc[0]['Imie']}", end='')
#     print(f" {group[1].iloc[0]['Liczba']}")
# print('')
# print("Chłopiec")
# print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])
# print("Dziewczynka")
# print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])

#zad3

df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')

print(df['Sprzedawca'].unique())
print('')
print(df.sort_values('Utarg', ascending=False).head(5))
print('')
print(df.groupby('Sprzedawca').size())
print('')
print(df.groupby('Kraj').agg({'Utarg': ['sum']}))
print(df.groupby('Kraj').size())
print('')
print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')].
      agg({'Utarg': ['sum']}))
print('')
print(df[df['Data zamowienia'].str[:4] == '2004'].agg({'Utarg': ['mean']}))
rok_2004 = df[((df[ 'Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
rok_2004.to_csv("zamowienia_2004.csv", index=False)
print(df2[(pd.DatetimeIndex(df2['Data zamowienia']).year == 2004)]['Utarg'].mean(axis=0))

df3=df2[(pd.DatetimeIndex(df2['Data zamowienia']).year == 2004)]

df4=df2[(pd.DatetimeIndex(df2['Data zamowienia']).year == 2005)]

df3.to_csv('zamówienia_2004.csv',index=False)

df4.to_csv('zamówienia_2005.csv',index=False)



