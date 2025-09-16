import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def analyze_text_with_gemini(text: str):
    # For initial development, return a mock, hard-coded result
    # In a real scenario, this would call the Gemini API
    print(f"Analyzing text with Gemini (mock): {text[:50]}...")
    return {
        "propaganda_score": 0.75,
        "identified_techniques": ["Bandwagon", "Ad Hominem"],
        "explanation": "This is a mock explanation for propaganda detection."
    }
