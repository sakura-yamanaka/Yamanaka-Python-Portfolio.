import streamlit as st
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.title("📰 News Article Sentiment Comparison Tool")

def article_text(source_type, source_content):
    if source_type == "URL":
        try:
            response = requests.get(source_content)
            soup = BeautifulSoup(response.text, 'html.parser')
            return ' '.join(p.get_text() for p in soup.find_all('p'))
        except Exception as e:
            st.error(f"Error fetching article: {e}")
            return ""
    elif source_type == "Upload" and source_content is not None:
        try:
            return source_content.read().decode("utf-8")
        except Exception as e:
            st.error(f"Error reading file: {e}")
            return ""
    return ""

def analyze_sentiment(text):
    sentiment = TextBlob(text)
    return sentiment.sentiment.polarity, sentiment.sentiment.subjectivity

def generate_wordcloud(text):
    wordcloud = WordCloud(width=600, height=300, background_color='white').generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    return fig

st.sidebar.header("Add Articles")

article_sources = []

num_articles = st.sidebar.number_input("How many articles do you want to compare?", min_value=2, max_value=10, value=2, step=1)

for i in range(num_articles):
    st.sidebar.markdown(f"### Article {i+1}")
    source_type = st.sidebar.radio(f"Input type for Article {i+1}", ["URL", "Upload"], key=f"source_type_{i}")
    if source_type == "URL":
        url = st.sidebar.text_input(f"Enter URL for Article {i+1}", key=f"url_{i}")
        article_sources.append(("URL", url))
    else:
        file = st.sidebar.file_uploader(f"Upload .txt for Article {i+1}", type="txt", key=f"file_{i}")
        if file:
            article_sources.append(("Upload", file))
        else:
            article_sources.append(("Upload", None))

# Process and visualize
results = []
for idx, (source_type, source) in enumerate(article_sources):
    if (source_type == "URL" and source) or (source_type == "Upload" and source is not None):
        text = article_text(source_type, source)
        polarity, subjectivity = analyze_sentiment(text)
        results.append({
            "label": f"Article {idx+1}",
            "text": text,
            "polarity": polarity,
            "subjectivity": subjectivity
        })

if len(results) == num_articles:
    st.subheader("📊 Sentiment Analysis Results")
    
    # Display polarity and subjectivity
    for article in results:
        st.markdown(f"**{article['label']}** — Polarity: `{article['polarity']:.2f}`, Subjectivity: `{article['subjectivity']:.2f}`")

    # Bar chart: polarity and subjectivity
    labels = [article["label"] for article in results]
    polarity = [article["polarity"] for article in results]
    subjectivity = [article["subjectivity"] for article in results]

    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots()
        ax1.bar(labels, polarity, color='lightblue')
        ax1.set_title("Polarity (Positive vs Negative Tone)")
        ax1.set_ylabel("Polarity")
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots()
        ax2.bar(labels, subjectivity, color='pink')
        ax2.set_title("Subjectivity (Opinion vs Fact)")
        ax2.set_ylabel("Subjectivity")
        st.pyplot(fig2)

    # Word Clouds
    st.subheader("☁️ Word Clouds")
    word_cols = st.columns(num_articles)
    for i, result in enumerate(results):
        with word_cols[i]:
            st.markdown(result["label"])
            st.pyplot(generate_wordcloud(result["text"]))