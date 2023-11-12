import pandas as pd
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline, make_pipeline
import joblib
import matplotlib.pyplot as plt
import numpy as np

# Charger les données
data_path = 'data/topic_classification_data.csv'
data = pd.read_csv(data_path)

# Utiliser les bons noms de colonnes
X = data['Text']
y = data['Category']

# Division en données d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Construction du pipeline de classification
pipeline = make_pipeline(TfidfVectorizer(stop_words='english'), RandomForestClassifier())

# Entraînement du modèle
pipeline.fit(X_train, y_train)

# Évaluation du modèle
predictions = pipeline.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions)}")

# Courbes d'apprentissage
train_sizes, train_scores, test_scores = learning_curve(pipeline, X, y, cv=5, scoring='accuracy', n_jobs=-1, train_sizes=np.linspace(0.1, 1.0, 10))

# Calcul de la moyenne et de l'écart-type pour les scores d'entraînement et de test
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

# Tracer les courbes d'apprentissage
plt.plot(train_sizes, train_mean, '--', color="#111111", label="Training score")
plt.plot(train_sizes, test_mean, color="#111111", label="Cross-validation score")

# Dessiner les bandes d'erreur
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, color="#DDDDDD")
plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, color="#DDDDDD")

# Titres et légendes
plt.title("Learning Curves")
plt.xlabel("Training Set Size"), plt.ylabel("Accuracy Score"), plt.legend(loc="best")
plt.tight_layout()

# Sauvegarder et afficher le graphique
plt.savefig('results/learning_curves.png')
plt.show()

# Sauvegarde du modèle
model_path = 'results/topic_classifier.pkl'
joblib.dump(pipeline, model_path)

print("Model trained and saved.")

# Charger le modèle entraîné
model_path = 'results/topic_classifier.pkl'
pipeline = joblib.load(model_path)

def classify_topics(text):
    """
    Classifie le sujet d'un texte donné en utilisant le modèle entraîné.
    
    :param text: Texte à classifier.
    :return: Sujet prédit.
    """
    # Assurez-vous que le texte est dans un format attendu par le modèle (ex. liste)
    predicted_topic = pipeline.predict([text])[0]
    return predicted_topic