import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def extract_top_keywords(texts, top_n=10):
    try:
        cv = CountVectorizer(max_df=0.8, stop_words='english')
        word_count = cv.fit_transform(texts)
        word_freq = zip(cv.get_feature_names_out(), word_count.sum(axis=0).tolist()[0])
        return sorted(word_freq, key=lambda x: -x[1])[:top_n]
    except Exception as e:
        print(f"Keyword extraction error: {e}")
        return []
