import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    try:
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        tokens = [word for word in text.split() if word not in STOPWORDS]
        return ' '.join(tokens)
    except Exception as e:
        print(f"[ERROR cleaning text]: {e}")
        return ""
