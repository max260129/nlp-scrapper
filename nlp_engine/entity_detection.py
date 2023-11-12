import spacy
import pandas as pd

# Charger le modèle SpaCy avec capacités NER
nlp = spacy.load("en_core_web_sm")

# Fonction pour détecter les entités ORG dans un texte
def detect_entities(text):
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    return entities

# Charger les données scrappées
data_path = 'scrapping/guardian_data.csv'  # Assurez-vous que le chemin est correct
news_data = pd.read_csv(data_path)

# Appliquer la détection d'entités sur chaque article
news_data['Organizations'] = news_data['Article Body'].apply(detect_entities)

# Sauvegarder les résultats enrichis dans le dossier data
news_data.to_csv('data/entity_detection.csv', index=False)

print("Entity detection completed and results saved in data folder.")
