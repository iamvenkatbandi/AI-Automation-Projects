import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def call_llm(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mixtral-8x7b-instruct",  # FREE model
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()['choices'][0]['message']['content']


def classify_email(email_text):
    prompt = f"""
    Classify this email into one category:
    support, sales, spam, general

    Email:
    {email_text}

    Only return the category.
    """

    return call_llm(prompt).strip()


def generate_reply(email_text, category):
    prompt = f"""
    You are a professional email assistant.

    Category: {category}

    Write a polite and professional reply for this email:
    {email_text}
    """

    return call_llm(prompt).strip()

def classify_email(email_text):
    prompt = f"""
    Classify this email into one category only:

    support
    sales
    spam
    job
    important
    ignore

    Email:
    {email_text}

    Only return one word.
    """

    return call_llm(prompt).strip().lower()
