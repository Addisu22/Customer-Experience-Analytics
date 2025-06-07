from src.scraper import fetch_reviews
from src.cleaner import clean_text
from src.sentiment_analyzer import get_sentiment
from src.feature_extractor import extract_top_keywords
from src.complaint_cluster import cluster_reviews
from src.db_handler import insert_to_oracle
import pandas as pd

APP_IDS = {
    'CBE': 'com.cbe.mobile',
    'BOA': 'com.boa.mobile',
    'Dashen': 'com.dashen.mobile'
}

if __name__ == "__main__":
    all_data = []
    for bank, app_id in APP_IDS.items():
        df = fetch_reviews(app_id, count=300)
        df['clean_text'] = df['content'].apply(clean_text)
        df['sentiment'] = df['clean_text'].apply(get_sentiment)
        df['bank'] = bank
        df['cluster'] = cluster_reviews(df['clean_text'].tolist())
        insert_to_oracle(df, "BANK_REVIEWS", "username/password@host:port/service")
        all_data.append(df)
    
    final_df = pd.concat(all_data)
    for bank in APP_IDS:
        keywords = extract_top_keywords(final_df[final_df['bank']==bank]['clean_text'])
        print(f"\nTop features for {bank}: {keywords}")
