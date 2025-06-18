from persona_profiles import PERSONAS

def chat_with_persona(persona_name, user_input, audio_file):
    if not persona_name:
        return "Please choose a persona."
    
    # Simulate a basic response for now
    response = f"{PERSONAS[persona_name]['name']} says: I hear you said '{user_input}'. Let's talk more."
    return response
