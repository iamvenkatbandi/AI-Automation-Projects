import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_text(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "AI Sheets Bot"
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 200
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        print("Status Code:", response.status_code)

        result = response.json()

        print("API Response:", result)

        if "choices" not in result:
            return f"Error: {result.get('error', result)}"

        return result["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"Exception occurred: {str(e)}"


def generate_ai_fields(input_text):
    prompt = f"""
    Analyze the following text and generate:

    1. A short summary (1 line)
    2. 3-5 relevant tags (comma separated)
    3. A catchy marketing caption

    Format strictly like this:
    Summary: ...
    Tags: ...
    Caption: ...

    Text:
    {input_text}
    """

    response = generate_text(prompt)

    try:
        lines = response.split("\n")

        summary = ""
        tags = ""
        caption = ""

        for line in lines:
            if "Summary:" in line:
                summary = line.replace("Summary:", "").strip()
            elif "Tags:" in line:
                tags = line.replace("Tags:", "").strip()
            elif "Caption:" in line:
                caption = line.replace("Caption:", "").strip()

        return summary, tags, caption

    except Exception as e:
        return "Error", "Error", "Error"
