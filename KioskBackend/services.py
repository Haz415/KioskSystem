from google.genai.errors import ClientError
from config import models, build_config
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_content(prompt,latitude,longitude):
    config = build_config( latitude, longitude)
    for model in models:
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config=config,
            )
            print(f"Used {model}")
            return response.text
        except ClientError as e:
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                print(f"{model} is rate limited. Trying next model...")
                continue
            raise
    raise RuntimeError("All models are rate limited. Try again later.")

