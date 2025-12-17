import google.generativeai as genai
from gtts import gTTS
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

async def test_gemini():
    print("Testing Gemini API...")
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel('gemini-flash-latest')
        response = await model.generate_content_async("Say hello")
        print(f"Gemini Success: {response.text}")
    except Exception as e:
        print(f"Gemini Failed: {e}")

async def test_tts():
    print("Testing TTS (gTTS)...")
    try:
        # Mimic utils.py logic
        def save():
            tts = gTTS(text="Hello world", lang='en')
            tts.save("test_gtts.mp3")
        await asyncio.to_thread(save)
        print("TTS Success: test_gtts.mp3 created")
    except Exception as e:
        print(f"TTS Failed: {e}")

async def main():
    await test_gemini()
    await test_tts()

if __name__ == "__main__":
    asyncio.run(main())
