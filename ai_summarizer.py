import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=api_key)


def generate_digest(news_articles):

    # Prepare news information for Gemini
    news_text = ""

    for index, article in enumerate(news_articles, start=1):
        news_text += f"""
        Article {index}
        Source: {article['source']}
        Title: {article['title']}
        Summary: {article['summary']}
        Link: {article['link']}
        """

    prompt = f"""
    You are a technology news analyst.

    Analyse the following technology news articles.

    Your tasks:

    1. Identify the 5 most important technology trends.
    2. Write exactly 5 bullet points summarizing them.
    3. Suggest 3 creative social media post ideas
       for a technology brand.
    4. Include relevant source links.
    5. Use simple, professional English.
    6. Do not invent facts or news.

    News articles:
    {news_text}
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text
