import seaborn as sns
import matplotlib.pyplot as plt

def plot_sentiment_distribution(df):
    sns.countplot(x='sentiment', hue='bank', data=df)
    plt.title("Sentiment Distribution by Bank")
    plt.show()
