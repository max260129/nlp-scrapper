import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

if not nltk.data.find('sentiment/vader_lexicon.zip'):
    nltk.download('vader_lexicon', quiet=True)

# Initialiser l'analyseur de sentiment VADER
sia = SentimentIntensityAnalyzer()

# Fonction pour analyser le sentiment d'un texte
def analyze_sentiment(text):
    sentiment_score = sia.polarity_scores(text)
    return sentiment_score['compound']  # Return the compound score



# Charger les données de nouvelles
data_path = 'data/entity_detection.csv'  # Assurez-vous que le chemin est correct
news_data = pd.read_csv(data_path)

# Appliquer l'analyse de sentiment
news_data['Title Sentiment'] = news_data['Headline'].apply(analyze_sentiment)
news_data['Body Sentiment'] = news_data['Article Body'].apply(analyze_sentiment)

# Sauvegarder les résultats dans un nouveau fichier CSV
news_data.to_csv('data/sentiment_analysis.csv', index=False)

print("Sentiment analysis completed and results saved in data folder.")
