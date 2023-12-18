import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')  # importarea datelor din fisierul data.csv

X = 6
Y = 10

# in primul grafic se afiseaza toate valorile
plt.figure(figsize=(15, 10))  # dimensionarea ferestrei
plt.plot(df.index, df['Durata'], label='Durata', marker='X', color='blue') #plot() deseneaza liniile intre punctele date ale graficului
plt.plot(df.index, df['Puls'], label='Puls', marker='X', color='red')
plt.plot(df.index, df['MaxPuls'], label='MaxPuls', marker='X', color='grey')
plt.plot(df.index, df['Calorii'], label='Calorii', marker='X', color='green')
plt.title('toate valorile')  # denumirea graficului
plt.legend()  # afisarea legendei graficului
plt.show() #afisarea graficului

# primele 6 valori pt toate valorile
plt.figure(figsize=(15, 10))  # dimensionarea ferestrei unde se va afisa graficul
plt.plot(df.index[:6], df['Durata'][:6], label='Durata', marker='X', color='blue')
plt.plot(df.index[:6], df['Puls'][:6], label='Puls', marker='X', color='red')
plt.plot(df.index[:6], df['MaxPuls'][:6], label='MaxPuls', marker='X', color='grey')
plt.plot(df.index[:6], df['Calorii'][:6], label='Calorii', marker='X', color='green')
plt.title('primele 6 valori')
plt.legend()
plt.show()

# ultimele 10 valori pt puls si durata
plt.figure(figsize=(15, 10))  # dimensionarea ferestrei unde se va afisa graficul
plt.plot(df.index[-10:], df['Durata'].tail(10), label='Durata', marker='X', color='blue')
plt.plot(df.index[-10:], df['Puls'].tail(10), label='Puls', marker='X', color='red')
plt.title('ultimele 10 valori')
plt.legend()
plt.show()
