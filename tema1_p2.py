import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#se citesc datele din fisierul CSV
df = pd.read_csv('data.csv')

# Se creaza o figura cu subplots
fig, axs = plt.subplots(3, 1, figsize=(12, 18))

# grafic pt primele 6 valori
X = 6
colors1 = plt.cm.viridis(np.linspace(0, 1, X))
df_head = df.head(X)
df_head.plot(x=df.columns[0], y=df.columns[1], kind='bar', ax=axs[0], color=colors1, edgecolor='black')
axs[0].set_title(f'Primele {X} valori')
axs[0].set_ylabel(df.columns[1])
axs[0].set_xlabel(df.columns[0])
axs[0].legend().set_visible(True)

# Adăugăm etichete cu valori pentru fiecare bară în subplotul 1
for i, val in enumerate(df_head[df.columns[1]]):
    axs[0].text(i, val + 0.1, str(val), ha='center', va='bottom')

# grafic 2: ultimele 10 valori
Y = 10
colors2 = plt.cm.inferno(np.linspace(0, 1, Y))
df_tail = df[['Durata', 'Puls']].tail(Y)
df_tail.plot(kind='bar', ax=axs[1], color=colors2, edgecolor='black')
axs[1].set_title(f'Ultimele {Y} valori pentru Durata si Puls')
axs[1].set_ylabel('Valoare')
axs[1].set_xlabel('Index')

# grafic pentru toate valorile
colors3 = plt.cm.plasma(np.linspace(0, 1, len(df)))
df.plot(x=df.columns[0], y=df.columns[1], kind='scatter', ax=axs[2], color=colors3, s=50, edgecolor='black', alpha=0.7)
axs[2].set_title('Toate valorile')
axs[2].set_ylabel(df.columns[1])
axs[2].set_xlabel(df.columns[0])

# afisarea graficelor
plt.tight_layout()
plt.show()
