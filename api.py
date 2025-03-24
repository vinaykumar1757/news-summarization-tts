from flask import Flask, request, jsonify
import json
from main import fetch_news, summarize_articles, perform_sentiment_analysis, generate_tts

app = Flask(__name__)

@app.route('/fetch_news', methods=['POST'])
def get_news():
    data = request.json
    company_name = data.get("company")
    articles = fetch_news(company_name)
    return jsonify(articles)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    articles = summarize_articles(data['articles'])
    return jsonify(articles)

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.json
    analyzed_articles = perform_sentiment_analysis(data['articles'])
    return jsonify(analyzed_articles)

@app.route('/tts', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data['text']
    filename = generate_tts(text)
    return jsonify({"audio_file": filename})

if __name__ == '__main__':
    app.run(debug=True)
