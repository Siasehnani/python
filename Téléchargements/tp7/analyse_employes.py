import pandas as pd  # Importer la bibliothèque Pandas

# Lire le fichier CSV
df = pd.read_csv('employes.csv')

# Afficher les 5 premières lignes du fichier
print("Les cinq premières lignes du fichier :")
print(df.head())

# Calculer et afficher la moyenne de l'âge des employés
moyenne_age = df['Âge'].mean()
print(f"\nLa moyenne d'âge des employés est : {moyenne_age:.2f} ans")
