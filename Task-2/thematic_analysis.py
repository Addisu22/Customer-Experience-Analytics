import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from utils import clean_text

def extract_keywords(texts, top_n=20):
    try:
        vectorizer = TfidfVectorizer(max_df=0.9, stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(texts)
        feature_names = vectorizer.get_feature_names_out()
        dense = tfidf_matrix.todense().tolist()
        
        keywords = {}
        for i, row in enumerate(dense):
            top_keywords = sorted(
                zip(feature_names, row), key=lambda x: x[1], reverse=True
            )[:top_n]
            keywords[i] = [word for word, score in top_keywords]
        return keywords
    except Exception as e:
        print(f"[ERROR extracting keywords]: {e}")
        return {}

def run_theme_pipeline(file_path):
    df = pd.read_csv(file_path)
    df['cleaned_review'] = df['review'].apply(clean_text)
    keywords_dict = extract_keywords(df['cleaned_review'])
    df['keywords'] = df.index.map(keywords_dict)
    
    # Manual example mapping of themes (simplified)
    def map_theme(keywords):
        themes = []
        if any(k in keywords for k in ['slow', 'crash', 'error']):
            themes.append('Performance')
        if any(k in keywords for k in ['login', 'password']):
            themes.append('Account Access')
        if any(k in keywords for k in ['interface', 'design']):
            themes.append('UI/UX')
        return ', '.join(themes) if themes else 'Other'
    
    df['theme'] = df['keywords'].apply(map_theme)
    df.to_csv('task_2/task2_output.csv', index=False)
    print("[INFO] Thematic analysis completed and saved.")
    return df

# Example usage
df_result = run_theme_pipeline('task-2/preprocessed_reviews.csv')
