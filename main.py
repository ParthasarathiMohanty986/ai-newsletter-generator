from summarizer import summarize_article

def main():
    article = {
        "summary": "Gemini is a new AI model developed by Google that can handle text, code, and image generation. It is designed to be integrated with Google products and is considered a strong competitor to other large language models in the AI space."
    }

    summary = summarize_article(article["summary"])
    print(f"\n📰 Summary:\n{summary}")

if __name__ == "__main__":
    main()
