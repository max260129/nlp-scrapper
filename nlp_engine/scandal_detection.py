import spacy
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Charger le modèle de langue SpaCy
nlp = spacy.load("en_core_web_sm")

# Mots-clés liés aux scandales environnementaux
keywords = [
    "pollution", "deforestation", "oil spill", "contamination", "environmental disaster",
    "toxic waste", "air pollution", "water pollution", "soil contamination", "chemical spill",
    "radiation leak", "industrial accident", "hazardous materials", "illegal dumping", "climate change",
    "global warming", "ozone depletion", "overfishing", "wildlife trafficking", "poaching",
    "endangered species", "habitat destruction", "illegal logging", "acid rain", "pesticide misuse",
    "ecosystem disruption", "biodiversity loss", "overhunting", "overcultivation", "land degradation",
    "desertification", "melting glaciers", "sea level rise", "coral bleaching", "marine pollution",
    "oil exploration", "fracking", "mining waste", "nuclear accident", "thermal pollution",
    "plastic pollution", "microplastics", "ocean acidification", "greenhouse gases", "methane emissions",
    "carbon footprint", "fossil fuels", "coal mining", "unsustainable practices", "energy waste",
    "resource depletion", "water scarcity", "drought", "floods", "natural habitat loss",
    "urban sprawl", "noise pollution", "light pollution", "air quality", "water quality",
    "soil erosion", "sedimentation", "heavy metals", "agricultural runoff", "eutrophication",
    "algal bloom", "dead zones", "fish kills", "invasive species", "ecological imbalance",
    "genetic modification", "GM crops", "pesticide resistance", "herbicide resistance", "industrial farming",
    "animal cruelty", "factory farming", "waste management", "landfills", "recycling failure",
    "renewable energy neglect", "sustainable development", "conservation failure", "environmental policy violation", "ecological footprint",
    "carbon emissions", "greenwashing", "environmental racism", "climate justice", "environmental activism suppression",
    "illegal trade", "wildlife exploitation", "forest fires", "arctic drilling", "ecosystem fragmentation"
]


# Fonction pour calculer l'embedding moyen d'un texte
def get_embedding(text):
    doc = nlp(text)
    embeddings = [token.vector for token in doc if not token.is_stop and not token.is_punct]
    if embeddings:
        return np.mean(embeddings, axis=0)
    else:
        return np.zeros((len(doc[0].vector),))  # Retourne un vecteur de zéros

# Calculer les embeddings pour les mots-clés
keywords_embeddings = [get_embedding(keyword) for keyword in keywords]

# Charger les données d'articles
data_path = 'scrapping/guardian_data.csv'
news_data = pd.read_csv(data_path)

# Fonction pour détecter les scandales dans un article
def detect_scandal(article):
    article_embedding = get_embedding(article)
    if np.any(np.isnan(article_embedding)):
        return False  # Retourne False si l'embedding est NaN
    for keyword_embedding in keywords_embeddings:
        similarity = cosine_similarity([article_embedding], [keyword_embedding])[0][0]
        if similarity > 0.7:  # Seuil de similarité à ajuster
            return True
    return False

# Appliquer la détection de scandales
news_data['Scandal'] = news_data['Article Body'].apply(detect_scandal)

# Sauvegarder les résultats
news_data.to_csv('results/scandal_detection.csv', index=False)

print("Scandal detection completed and results saved.")
