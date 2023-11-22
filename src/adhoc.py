import pandas as pd
import json


def find_journal(json_path):
    """
    Trouve et affiche le journal qui mentionne le plus grand nombre de médicaments différents.
    
    :param json_path: Chemin vers le fichier JSON contenant les données.
    """
    try:
        with open(json_path, 'r') as file:
            data = json.load(file)
    except Exception as e:
        print(f"Erreur lors du chargement du fichier JSON : {e}")
        return

    # Création d'un DataFrame et traitement des données
    data_df = pd.DataFrame(data['drugs_in_journal'])
    journal_counts = data_df.groupby('journal').count().sort_values(by='drug', ascending=False).reset_index()

    # Récupération des informations à printer
    journal_name = journal_counts.iloc[0]['journal']
    drug_count = journal_counts.iloc[0]['drug']

    print(f"Le journal qui parle du plus de médicaments différents est {journal_name} avec {drug_count} médicaments")
