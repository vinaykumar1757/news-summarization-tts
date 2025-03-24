import streamlit as st
import requests
from transformers import pipeline
from gtts import gTTS
import os
from deep_translator import GoogleTranslator
from utils import fetch_news

sentiment_model = pipeline("sentiment-analysis")

def summarize_articles(articles):
    """Generates structured summaries for the articles."""
    summarized_articles = []
    
    for article in articles:
        summary = article["content"] if len(article["content"]) > 10 else "No summary available"
        summarized_articles.append({
            "title": article["title"],  
            "summary": summary  
        })
    
    return summarized_articles


def perform_sentiment_analysis(articles):
    for article in articles:
        if len(article["summary"].strip()) > 10:
            result = sentiment_model(article["summary"])[0]
            article["sentiment"] = result["label"]
        else:
            article["sentiment"] = "Unknown"
    return articles


def generate_tts(articles, lang='hi'):
    sentences = []

    for article in articles:
        hindi_summary = GoogleTranslator(source="en", target="hi").translate(article['summary'])
        sentences.append(f"{article['title']}। {hindi_summary}।") 

    full_text = " ".join(sentences)

    tts = gTTS(text=full_text, lang=lang, slow=False)
    filename = "output.mp3"
    tts.save(filename)
    return filename

st.title("News Summarization & Sentiment Analysis")

company_name = st.text_input("Enter a company name:")

if st.button("Fetch News"):
    articles = fetch_news(company_name)
    
    if not articles:
        st.error("No news found for the given company!")
    else:

        summarized_articles = summarize_articles(articles)
        analyzed_articles = perform_sentiment_analysis(summarized_articles)

        st.subheader(f"Company_Name: {company_name}")
        for article in analyzed_articles:
            st.write(f"Title: {article['title']}")
            st.write(f"Summary: {article['summary']}")
            st.write(f"Sentiment: {article['sentiment']}")
            st.write("---")

        tts_file = generate_tts(analyzed_articles)

        st.audio(tts_file, format="audio/mp3")
