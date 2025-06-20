# chat_logic.py

import os
from openai import OpenAI
from persona_profiles import PERSONAS
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

def chat_with_persona(persona_name, user_input, audio_file=None):
    persona = PERSONAS[persona_name]

    prompt = (
        f"You are {persona['name']}, a fictional person. "
        f"Here is your background:\n{persona['backstory']}\n\n"
        f"Someone is having a friendly conversation with you. "
        f"Respond realistically to this message:\n\n"
        f"{user_input}"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}],
            temperature=0.8,
            max_tokens=150
        )
        reply = response.choices[0].message.content.strip()
        return reply
    except Exception as e:
        return f"(Error generating response: {str(e)})"
