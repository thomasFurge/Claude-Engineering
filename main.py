import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import pandas as pd

df = pd.read_csv('Nais2018.csv', delimiter=';')
df = df.loc[(df['JRECC'] > 0) & (df['MNAIS'] == 10)]  #on enlève les enfants non reconnus

df_garcon = df.loc[df['SEXE'] == 1]
df_fille = df.loc[df['SEXE'] == 2]

df_jm_garcon = df_garcon.groupby(['JRECC']).size()
df_jm_fille = df_fille.groupby(['JRECC']).size()

print(df_jm_garcon.sum())
print(df_jm_fille.sum())

fig = plt.figure()
gs = GridSpec(nrows=2, ncols=2)
ax0 = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[:, 1])
ax2 = fig.add_subplot(gs[1, 0])
ax = [ax0, ax1, ax2]

#### COURBES NAISSANCES
df_jm_garcon.plot(figsize=(14, 6), color='blue', ax=ax[0], label='Naissances garcons')
df_jm_fille.plot(figsize=(14, 6), color='pink', ax=ax[0], label='Naissances filles')

ax[0].axvline(25, linestyle='--', color='red', label='Date du terme')

weekends = [
    (6, 7),
    (13, 14),
    (20, 21),
    (27, 28)
]

ax[0].fill_between([weekends[0][0], weekends[0][1]], [351, 351], alpha=0.2, label='weekend', color='green')

for (debut, fin) in weekends[1:]:
    ax[0].fill_between([debut, fin], [351, 351], alpha=0.2, color='green')

ax[0].legend()
ax[0].set_title('Claude Engineering - Stats Octobre 2018')

#### REPARTITION
nb_garcons = df_jm_garcon.sum()
nb_filles = df_jm_fille.sum()

total = (nb_filles+nb_garcons)
pt_garcon = round(nb_garcons/total * 100, 4)
pt_fille = round(nb_filles/total * 100, 4)

width = 100

ax[1].bar(-width/2, nb_garcons, width, color='blue', label=str(pt_garcon) + '% de garçons')
ax[1].bar(width/2, nb_filles, width, color='pink', label=str(pt_fille) + '% de filles')

ax[1].legend()
ax[1].set_title('Pourcentage Octobre 2018')

#### Courbes 2020

ax[2].axvline(25, linestyle='--', color='red', label='Date du terme')

weekends = [
    (3, 4),
    (10, 11),
    (17, 18),
    (24, 25)
]

ax[2].fill_between([weekends[0][0], weekends[0][1]], [351, 351], alpha=0.2, label='weekend', color='green')

for (debut, fin) in weekends[1:]:
    ax[2].fill_between([debut, fin], [351, 351], alpha=0.2, color='green')

ax[2].plot(1, 0)
ax[2].plot(31, 0)

ax[2].legend()
ax[2].set_title('Claude Engineering - Stats Octobre 2020')

plt.show()
