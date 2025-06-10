import streamlit as st
from rss_fetcher import get_articles
from summarizer import summarize_article
from formatter import generate_html

st.set_page_config(page_title="AI Newsletter Generator")

st.title("📰 AI-Powered Newsletter Generator")

category = st.selectbox("Choose News Category", ["Tech", "Sports"])

if st.button("Generate Newsletter"):
    with st.spinner("Fetching articles and generating summaries..."):
        articles = get_articles(category)
        summarized_articles = []

        for article in articles:
            try:
                summary = summarize_article(article["summary"])
            except Exception as e:
                summary = "Summary not available"
                st.error(f"❌ Error generating summary: {e}")
            summarized_articles.append({
                "title": article["title"],
                "link": article["link"],
                "summary": summary
            })

        html_content = generate_html(summarized_articles, title=f"{category} News Digest")
        st.components.v1.html(html_content, height=600, scrolling=True)
