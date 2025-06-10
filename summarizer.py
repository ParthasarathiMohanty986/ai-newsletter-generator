import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Correct configuration using the environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use Gemini Pro model
model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")

def summarize_article(article_text):
    try:
        prompt = f"Summarize this article:\n\n{article_text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("❌ Error generating summary:", e)
        return "Summary not available"
    
