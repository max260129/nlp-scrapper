# NLP-Enriched News Intelligence Platform

## Introduction
The NLP-Enriched News Intelligence Platform is a sophisticated tool designed to enhance the analysis of news articles using advanced Natural Language Processing (NLP) techniques. This platform leverages various NLP methodologies to extract entities, analyze sentiments, classify topics, and detect potential environmental scandals in news articles.

## Features
- **Entity Detection**: Identify organizations mentioned in news articles.
- **Sentiment Analysis**: Analyze and score the sentiment conveyed in news headlines and content.
- **Topic Classification**: Classify news articles into predefined categories such as Sports, Tech, Business, etc.
- **Scandal Detection**: Detect mentions of environmental scandals in news content.

## Project Structure
```
nlp-scrapper/
│
├── all.py                 # Main script to run the entire NLP pipeline
├── README.md              # This file
│
├── data/                  # Data files and input CSVs
│   ├── entity_detection.csv
│   ├── sentiment_analysis.csv
│   └── topic_classification_data.csv
│
├── nlp_engine/            # NLP processing scripts
│   ├── entity_detection.py
│   ├── scandal_detection.py
│   ├── sentiment_analysis.py
│   └── topic_classification.py
│
├── results/               # Output files and generated reports
│   ├── enhanced_news.csv
│   ├── learning_curves.png
│   ├── scandal_detection.csv
│   └── topic_classifier.pkl
│
└── scrapping/             # Web scraping scripts
    ├── guardian_data.csv
    └── scrapper_news.py
```

## Getting Started

### Prerequisites
- Python 3.x
- Libraries: pandas, NLTK, scikit-learn, Matplotlib

### Installation
1. Clone the repository:
   ```
   git clone [repository URL]
   ```
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

### Usage
Run the main script to process the news articles:
```
python all.py
```

## How It Works
- **Scrapping**: The `scrapper_news.py` script fetches news articles from predefined sources.
- **Entity Detection**: `entity_detection.py` identifies organizations and other key entities in the news content.
- **Sentiment Analysis**: `sentiment_analysis.py` evaluates the sentiments expressed in the news articles.
- **Topic Classification**: `topic_classification.py` categorizes the articles into different topics.
- **Scandal Detection**: `scandal_detection.py` scans for mentions of environmental scandals.

## Contributions
Contributions are welcome! Please read the contribution guidelines for more information.

## License
This project is licensed under the [LICENSE NAME] - see the LICENSE file for details.
