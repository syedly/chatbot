import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
AI_API_KEY = os.getenv('AI_API_KEY')

llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    tempreture=0.5,
    verbose=True,
    streaming=True,
    ai_api_key=AI_API_KEY,
)