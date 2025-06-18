import os
from elevenlabs import generate, play, set_api_key
from dotenv import load_dotenv

load_dotenv()
set_api_key(os.getenv("ELEVEN_API_KEY"))

def speak_text(text, voice_id):
    try:
        audio = generate(text=text, voice=voice_id)
        play(audio)
    except Exception as e:
        print(f"❌ Error during TTS: {e}")
