import pandas as pd
import os

# Dossier contenant les fichiers CSV
dossier = "/home/yann/Documents/YUGIOH-DB/propre"

# Liste tous les fichiers CSV
fichiers = [f for f in os.listdir(dossier) if f.endswith('.csv')]

# Lis et concatène tous les fichiers
df_total = pd.concat([pd.read_csv(os.path.join(dossier, f)) for f in fichiers])

# Sauvegarde dans un nouveau fichier
df_total.to_csv("fichiers-combines.csv", index=False)

