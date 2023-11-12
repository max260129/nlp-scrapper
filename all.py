import os
import pandas as pd
from nlp_engine.entity_detection import detect_entities
from nlp_engine.sentiment_analysis import analyze_sentiment
from nlp_engine.topic_classification import classify_topics
from nlp_engine.scandal_detection import detect_scandal

# Définir le chemin du projet
project_dir = '/home/maxx/Code/Zone01/AI/nlp-scrapper'

# Exécuter le script de scraping
os.system(f'python {project_dir}/scrapping/scrapper_news.py')

# Charger les données scrappées
scrapped_data_path = f'{project_dir}/scrapping/guardian_data.csv'
news_data = pd.read_csv(scrapped_data_path)

# Parcourir chaque article et appliquer les traitements NLP
for index, row in news_data.iterrows():
    print(f"\nEnriching {row['URL']}:")

    # Détection des entités
    entities = detect_entities(row['Article Body'])
    print("---------- Detect entities ----------")
    print(f"Detected {len(entities)} companies which are {', '.join(entities)}")

    # Classification des sujets
    topic = classify_topics(row['Article Body'])
    print("\n---------- Topic detection ----------")
    print(f"The topic of the article is: {topic}")

    # Sentiment analysis
    print("\n---------- Sentiment analysis ----------")
    sentiment_title = analyze_sentiment(row['Headline'])
    print(f"The title sentiment is: {sentiment_title}")
    sentiment_body = analyze_sentiment(row['Article Body'])
    print(f"The body of the article sentiment is: {sentiment_body}")

    # Détection de scandales
    scandal_detected = detect_scandal(row['Article Body'])
    print("\n---------- Scandal detection ----------")
    if scandal_detected:
        print("Environmental scandal detected.")
    else:
        print("No environmental scandal detected.")

# Load the scraped data
data_path = 'scrapping/guardian_data.csv'
news_data = pd.read_csv(data_path)

# Lists to store the enriched information
entities_list = []
topics_list = []
sentiment_title_list = []
sentiment_body_list = []
scandal_list = []

# Process each article
for index, row in news_data.iterrows():
    #print(f"\nEnriching {row['URL']}:")

    # Entity Detection
    entities = detect_entities(row['Article Body'])
    entities_list.append(', '.join(entities))

    # Topic Classification
    topic = classify_topics(row['Article Body'])
    topics_list.append(topic)

    # Sentiment Analysis
    sentiment_title = analyze_sentiment(row['Headline'])
    sentiment_title_list.append(sentiment_title)
    sentiment_body = analyze_sentiment(row['Article Body'])
    sentiment_body_list.append(sentiment_body)

    # Scandal Detection
    scandal_detected = detect_scandal(row['Article Body'])
    scandal_list.append(scandal_detected)

# Add the enriched data to the DataFrame
news_data['Entities'] = entities_list
news_data['Topic'] = topics_list
news_data['Title Sentiment'] = sentiment_title_list
news_data['Body Sentiment'] = sentiment_body_list
news_data['Scandal Detected'] = scandal_list

# Save the enriched DataFrame to a CSV file
enhanced_news_path = 'results/enhanced_news.csv'
news_data.to_csv(enhanced_news_path, index=False)

print("\nAll news articles have been processed and the results are saved in enhanced_news.csv.")
