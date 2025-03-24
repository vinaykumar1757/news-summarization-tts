🚀 Project Overview
This web app extracts real-time news articles for a given company, performs sentiment analysis, and generates Hindi Text-to-Speech (TTS) summaries. The app is deployed on Hugging Face Spaces and built using:
✅ Streamlit for the web UI
✅ BeautifulSoup / NewsAPI for news extraction
✅ Hugging Face Transformers for sentiment analysis
✅ Deep Translator for English-to-Hindi translation
✅ gTTS for Hindi speech generation

🎯 Features
✔ Fetch news articles dynamically (using NewsAPI or web scraping)
✔ Summarize articles for quick insights
✔ Perform sentiment analysis (Positive / Negative / Neutral)
✔ Generate Hindi audio summaries
✔ Interactive UI with Streamlit
✔ Deployed on Hugging Face Spaces

🛠️ Setup Instructions
🔹 1. Clone the Repository
git clone https://github.com/vinaykumar1757/news-summarization-tts.git
cd news-summarization-tts
🔹 2. Install Dependencies
pip install -r requirements.txt
🔹 3. Set Up API Keys (If Using NewsAPI)
If you're using NewsAPI for news extraction, create a .env file and add:
NEWS_API_KEY=your_news_api_key_here
🔹 4. Run the Application Locally
streamlit run app.py
📌 Project Structure
📂 news-summarization-tts
 ├── 📜 app.py                # Main Streamlit app
 ├── 📜 utils.py              # Utility functions for news fetching
 ├── 📜 api.py                # API routes (if needed)
 ├── 📜 requirements.txt      # Dependencies
 ├── 📜 README.md             # Documentation
 ├── 📜 .env                  # API keys (if using NewsAPI)
