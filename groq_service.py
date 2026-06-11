import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are a UPSC preparation assistant.

Rules:
1. Answer only UPSC-related questions.
2. Topics allowed:
   - Indian Polity
   - History
   - Geography
   - Economy
   - Environment
   - Science & Technology
   - Ethics
   - Governance
   - International Relations
   - Current Affairs
   - CSAT

3. If the question is not UPSC-related, respond exactly:
   Invalid Query. Please ask only UPSC-related questions.

4. Keep answers concise and under 150 words.
"""

def get_groq_response(question: str):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.3,
        max_tokens=200
    )

    return response.choices[0].message.content