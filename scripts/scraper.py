import pandas as pd
from google_play_scraper import Sort, reviews
import time

def fetch_reviews(app_id, count=500):
    all_reviews = []
    try:
        for i in range(0, count, 100):
            result, _ = reviews(
                app_id,
                lang='en',
                country='us',
                sort=Sort.NEWEST,
                count=100
            )
            all_reviews.extend(result)
            time.sleep(1)  # avoid throttling
    except Exception as e:
        print(f"Error fetching reviews: {e}")
    
    return pd.DataFrame(all_reviews)[['userName', 'content', 'score', 'at', 'reviewCreatedVersion']]
