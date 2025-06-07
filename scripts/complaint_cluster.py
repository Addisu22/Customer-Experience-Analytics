from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_reviews(texts, num_clusters=5):
    try:
        tfidf = TfidfVectorizer(stop_words='english')
        X = tfidf.fit_transform(texts)
        kmeans = KMeans(n_clusters=num_clusters, random_state=0)
        clusters = kmeans.fit_predict(X)
        return clusters
    except Exception as e:
        print(f"Clustering error: {e}")
        return [-1]*len(texts)
