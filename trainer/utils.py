import google.generativeai as genai
from gtts import gTTS
import asyncio
import os
import uuid
from django.conf import settings

# Configure Gemini
def configure_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
    genai.configure(api_key=api_key)

async def generate_meditation_script(mood):
    configure_gemini()
    # Using the latest available flash model
    model = genai.GenerativeModel('gemini-flash-latest')
    prompt = f"Write a short, calming 1-minute meditation script for someone feeling {mood}. The script should be soothing and direct. Do not include 'narrator' labels or stage directions, just the spoken words."
    response = await model.generate_content_async(prompt)
    return response.text

async def generate_audio(text, voice):
    # Mapping voices to gTTS accents (tld)
    # en-US -> com
    # en-GB -> co.uk
    tld = 'com'
    if 'GB' in voice:
        tld = 'co.uk'

    output_filename = f"meditation_{uuid.uuid4()}.mp3"
    output_path = os.path.join(settings.MEDIA_ROOT, output_filename)
    
    # Ensure media directory exists
    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
    
    def save_audio():
        tts = gTTS(text=text, lang='en', tld=tld)
        tts.save(output_path)
    
    await asyncio.to_thread(save_audio)
    
    return os.path.join(settings.MEDIA_URL, output_filename)
