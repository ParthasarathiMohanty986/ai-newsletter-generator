
📰 AI-Powered Newsletter Generator

An end-to-end Python project that fetches real-time news from RSS feeds, summarizes articles using Google Gemini AI, and renders them as a clean, dynamic newsletter via a Streamlit web app.

 🚀 Features

  🔍 Fetches latest news based on category (Tech, Sports, Business)
  🧠 Summarizes articles using **Google Gemini AI**
  📝 Renders a responsive HTML newsletter using **Jinja2**
  🌐 Interactive frontend using **Streamlit**
  ⚙️ Modular and clean architecture

 🛠 Tech Stack

| Component          | Tech Used              | Purpose                              |
|--------------------|------------------------|--------------------------------------|
| Core Language      | Python 3.10+           | Backend and app logic                |
| RSS Parsing        | `feedparser`           | Fetches news articles via RSS        |
| AI Summarization   | `google.generativeai`  | Summarizes article content           |
| Template Engine    | `Jinja2`               | Formats HTML newsletters             |
| Frontend Interface | `Streamlit`            | Web UI for category selection, display |
| HTML Rendering     | `Streamlit Components` | Embeds generated HTML inside Streamlit |

 📁 Project Structure

newsletter\_project/
│
├── app.py                 # Streamlit frontend app
├── rss\_fetcher.py         # RSS feed logic
├── summarizer.py          # Gemini summarization
├── formatter.py           # Jinja2 HTML formatter
├── templates/
│   └── newsletter\_template.html  # HTML template
├── .env                   # Your Gemini API key (optional)
└── requirements.txt       # Python dependencies

 🧑‍💻 How It Works

1. **User selects a news category** (e.g., Tech) on Streamlit.
2. `rss_fetcher.py` pulls articles from a matching RSS feed.
3. `summarizer.py` uses **Google Gemini API** to summarize the content.
4. `formatter.py` renders these summaries into an HTML newsletter using **Jinja2**.
5. `app.py` displays the final newsletter inside Streamlit.

 
⚙️ Setup Instructions

1. Clone this repo
   bash
   git clone https://github.com/yourusername/newsletter-generator.git
   cd newsletter-generator


2. Create a virtual environment
    bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   

3. Install dependencies

   bash
   pip install -r requirements.txt
   

4. Set your Gemini API key**

    Get a free API key from [Google AI Studio](https://makersuite.google.com/app)
    Either:

      Set as environment variable:
       `export GOOGLE_API_KEY=your-key`
     Or replace directly inside `summarizer.py`

5. Run the app

   bash
   streamlit run app.py
   

🧠 To Do / Future Features

* 🔄 Allow user to input custom RSS feeds
* 📧 Send newsletter via email (SMTP integration)
* 🧱 Store past newsletters using SQLite or MongoDB
* 🎨 Toggle dark/light themes in Streamlit
* 🌍 Multi-language support (using Gemini translation)



  ![image](https://github.com/user-attachments/assets/4981a8ea-6a59-4de7-ba65-52c5515cf454)
  ![image](https://github.com/user-attachments/assets/04ecbceb-fe81-403b-8ac8-4a658bdb2d3e)


