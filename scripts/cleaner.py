import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def clean_text(text):
    try:
        text = re.sub(r"http\S+|[^a-zA-Z\s]", "", text.lower())
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(w) for w in text.split() if w not in stop_words]
        return " ".join(words)
    except Exception as e:
        print(f"Text cleaning error: {e}")
        return ""
