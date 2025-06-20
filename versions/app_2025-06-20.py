def chat_with_persona(persona_name, user_input, audio_file):
    from persona_profiles import PERSONAS

    persona = PERSONAS.get(persona_name)
    if not persona:
        return "I'm not sure who you're talking to."

    name = persona.get("name", persona_name)
    backstory = persona.get("backstory", "")

    # Basic keyword triggers (expand as needed)
    lowered = user_input.lower()
    if "god" in lowered or "faith" in lowered:
        return f"{name} pauses. 'You know, I've had questions about that for a while. What makes you bring that up?'"
    elif "church" in lowered or "bible" in lowered:
        return f"{name} looks curious. 'I haven’t been to church in years. What’s it like for you?'"
    elif "hell" in lowered:
        return f"{name} frowns. 'That’s a hard topic. Do you really believe my grandmother is in hell?'"
    elif "jesus" in lowered:
        return f"{name} says quietly, 'He’s a complicated figure for me. I’m not sure what to believe.'"
    elif "love" in lowered:
        return f"{name} reflects, 'Everyone talks about love, but it feels rare. What does it mean to you?'"
    elif "life" in lowered or "death" in lowered:
        return f"{name} nods slowly. 'Big questions. Do you think there’s more to life than what we see?'"
    else:
        return f"{name} hears you say: '{user_input}' and responds: 'Let’s talk more about that.'"
