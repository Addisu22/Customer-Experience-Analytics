import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from utils import clean_text

def analyze_sentiment(text):
    try:
        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(text)['compound']
        if score >= 0.05:
            return 'positive', score
        elif score <= -0.05:
            return 'negative', score
        else:
            return 'neutral', score
    except Exception as e:
        print(f"[ERROR in sentiment analysis]: {e}")
        return 'neutral', 0

def run_sentiment_pipeline(file_path):
    df = pd.read_csv(file_path)
    df['cleaned_review'] = df['review'].apply(clean_text)
    df[['sentiment', 'sentiment_score']] = df['cleaned_review'].apply(
        lambda x: pd.Series(analyze_sentiment(x))
    )
    df.to_csv('task_2/sentiment_output.csv', index=False)
    print("[INFO] Sentiment analysis completed and saved.")
    return df
