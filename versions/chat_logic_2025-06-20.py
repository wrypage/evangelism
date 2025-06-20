# chat_logic.py

import os
from openai import OpenAI
from persona_profiles import PERSONAS
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_persona(persona_name, user_input, history=None):
    persona = PERSONAS.get(persona_name)
    if not persona:
        return "I don't know who you're talking to."

    name = persona.get("name", persona_name)
    tone = persona.get("tone", "neutral")
    backstory = persona.get("backstory", "")

    # Create the system message to guide the persona's tone and character
    system_prompt = (
        f"You are {name}, a person who is {tone}. "
        f"Here is your background: {backstory} "
        "Respond naturally, like a real person having a conversation. Be consistent with your personality. "
        "Do not explain you're an AI. Engage honestly in first person."
    )

    # Build conversation messages
    messages = [{"role": "system", "content": system_prompt}]
    if history:
        for user_msg, persona_msg in history:
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": persona_msg})

    # Append the latest user input
    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.9,
        )
        reply = response.choices[0].message.content.strip()
        return reply
    except Exception as e:
        return f"{name}: Hmm... I'm trying to figure out how to respond, but something went wrong. ({e})"
