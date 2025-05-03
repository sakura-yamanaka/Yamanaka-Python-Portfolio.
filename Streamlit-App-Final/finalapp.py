# Import necessary libraries
import streamlit as st
from textblob import TextBlob # For sentiment analysis
import requests # For getting article text from a URL
from bs4 import BeautifulSoup # For parsing HTML and extracting text
import matplotlib.pyplot as plt # For plotting bar charts
from wordcloud import WordCloud # For generating word clouds

# Page title and description
st.title("📰 News Article Sentiment Comparison Tool")
st.write("""
    Welcome to the easy-to-use **News Article Sentiment Comparison Tool**! The steps are simple: 
""")
# Instructions for using the app
st.write("""
         1) Choose how many articles you want to compare
         2) Input article urls or upload .txt files 
         3) Watch as this tool analyzes the articles, compares the sentiments using a bar plot, and creates a word cloud!
""")

# Definition of sentiment terms so users can understand the results
st.subheader("🔑 Key Terms:")
st.write("**Polarity Score**: Measures the emotional tone: positive vs. negative.")
st.write("**Subjectivity Score**: Measures the degree of opinion vs. fact.")
st.markdown("---")

# Create function for processing new article text
def article_text(source_type, source_content):
    #For getting article text from a URL
    if source_type == "URL":
        try:
            response = requests.get(source_content)
            # Using BeautifulSoup to parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extracting text from all paragraphs by combing them into one string
            return ' '.join(p.get_text() for p in soup.find_all('p'))
        # Handling potential errors
        except Exception as e:
            st.error(f"Error fetching article: {e}")
            return ""
    #For getting article text from an uploaded .txt file
    elif source_type == "Upload" and source_content is not None:
        try:
            # Reading the uploaded file
            return source_content.read().decode("utf-8")
        # Handling potential errors
        except Exception as e:
            st.error(f"Error reading file: {e}")
            return ""
    return ""

# Create function for analyzing sentiment
def analyze_sentiment(text):
    # Using TextBlob to analyze sentiment 
    sentiment = TextBlob(text)
    # Getting both polarity and subjectivity scores
    return sentiment.sentiment.polarity, sentiment.sentiment.subjectivity

# Create function for generating word clouds
def generate_wordcloud(text):
    wordcloud = WordCloud(width=600, height=300, background_color='white').generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    return fig

# Sidebar for user input of news articles
st.sidebar.header("Add Articles")

# Initialize list to store article sources
article_sources = []

# Sidebar for selecting number of articles that the user wants to compare
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
    st.subheader("📊 Sentiment Analysis Results:")

    # Display polarity and subjectivity
    for article in results:
        st.markdown(f"**{article['label']}** — Polarity: `{article['polarity']:.2f}`, Subjectivity: `{article['subjectivity']:.2f}`")
        
        if article["subjectivity"] > 0.6:
            st.markdown("_This article leans heavily on opinions._")
        else:
            st.markdown("_This article is more factual._")
        
        # Interpretation of polarity
        if article["polarity"] > 0.6:
            st.markdown("_This article has a strongly positive tone._")
        elif article["polarity"] < -0.6:
            st.markdown("_This article has a strongly negative tone._")
        else:
            st.markdown("_This article has a neutral or mixed tone._")

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