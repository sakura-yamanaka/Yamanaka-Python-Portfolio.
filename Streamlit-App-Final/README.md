# Streamlit Final Project: Political News Article Sentiment Comparison Tool

![Article](images/TitlePicture.png)

## Contents: 
- [Project Overview](#project-overview)
- [App Features](#app-features)
- [Instructions](#instructions)
- [Visuals](#visuals)
- [References](#references)

## Project Overview 
This project focuses on building a **Political News Article Sentiment Comparison Tool**. The goal was to create an interactive app that allows users to upload or input political news articles and then get sentiment analysis of the polarity score (how negative or posititve) the article is and then subjkectivity score (how opiniated vs, factual) the article is. Lastly, the tool creates a word cloud of the most frequently used words in the article. 

### What problem does this solve? 
Political news articles have become **increasingly polarized in recent years.** Many sources frame events as either strongly positive or negative, often to advance a particular agenda. Furthermore, articles often blur the line between opinion and fact, leading news consumers to unknowingly be swayed by biased narratives. 

The **Political News Article Sentiment Comparison Tool** directly addresses this issue by providing readers with a clear, data-driven assessment of an article’s sentiment and subjectivity. By analyzing the polarity (positive or negative tone) and subjectivity (degree of opinion vs. fact), the tool helps users critically evaluate the content they encounter. Additionally, the word cloud highlights key terms, offering a visual representation of the article’s main focus. By allowing users to compare multiple articles,  users can identify which ones are more objective and fact-based. This comparison empowers users to seek out more balanced sources, fostering independent thinking, and mitigating the effects of media polarization.

## App Features

### Upload or Input Text

Users can either paste the URL of a political news article or upload a .txt file directly into the app. The tool then extracts and processes the article text for analysis.

### Compare Multiple Articles

Users can choose to analyze and compare 2 to 10 articles at once. This side-by-side comparison helps highlight differences in tone, subjectivity, and keyword usage across various sources. This is especially useful when comparing articles from different sources covering the same event. 

### Automatic Sentiment Analysis

Using the TextBlob library, the app calculates each article’s:

- Polarity Score (ranging from -1 to 1): Indicates whether the article’s tone is more negative, neutral, or positive.
- Subjectivity Score (ranging from 0 to 1): Reflects how factual or opinionated the article is.

The app also provides brief interpretations of the results—for example, whether an article "has a strongly positive tone" or “leans heavily on opinions."

### Visualize Sentiment with Bar Charts

Polarity and subjectivity scores for all articles are displayed in side-by-side bar charts. This makes it easy to visually compare tone and objectivity across multiple sources at a glance.

### Generate Word Clouds

For each article, the app generates a word cloud to highlight the most frequently used words. Larger words indicate higher frequency, giving users quick insight into each article’s key themes and focus.

**Together, these features give users a powerful, accessible tool to critically assess political news content.**

## Instructions 
To run this app, you can either run the app locally or access the deployed version. The instructions for each are below.  

### Option 1: Running the App Locally 

1. Clone or download the `finalapp.py` file from this GitHub repository to your local machine.

2. Install the necessary libraries by running the following commands in your terminal:

    ```bash
    pip install streamlit
    pip install textblob
    pip install requests
    pip install beautifulsoup4
    pip install matplotlib
    pip install wordcloud
    ```

3. Run the app in the terminal:
    ```bash
    streamlit run finalapp.py
    ```

4. Open your browser and go to `http://localhost:8501` to interact with the app.

### Option 2: Accessing the Deployed Version

1. Open the deployed version of the app on Streamlit Community Cloud using this [link](https://yamanaka-python-portfolio-rkb34gwgotslwkrqsrufdu.streamlit.app) 

## Visuals 

### App Interface:
![AppInterface](images/AppInterface.png)

### Example of Use:  
![ExamplePic1](images/ExamplePic1.png)

![ExamplePic2](images/ExamplePic2.png)

## References
- [Generating Word Cloud in Python](https://www.geeksforgeeks.org/generating-word-cloud-python/)
- [SENTIMENT ANALYSIS USING PYTHON](https://www.newscatcherapi.com/blog/sentiment-analysis-using-python)
- [Tutorial: Quickstart -- TextBlob](https://textblob.readthedocs.io/en/dev/quickstart.html#quickstart)
- [API Reference -- TextBlob](https://textblob.readthedocs.io/en/dev/api_reference.html#textblob.blob.TextBlob.sentiment)
- [BeautifulSoup - Scraping List from HTML](https://www.geeksforgeeks.org/beautifulsoup-scraping-link-from-html/)
- [Implementing Web Scraping in Python with BeautifulSoup](https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/)
- [Markdown Extended Syntax – Markdown Guide](https://www.markdownguide.org/extended-syntax/)
