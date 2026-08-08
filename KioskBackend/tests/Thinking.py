from google import genai
from google.genai import types
from google.genai.errors import ClientError
import os
from dotenv import load_dotenv

load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


models = [
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
    "gemini-3-flash-preview"
]

prompt = "can you find me the route to Japan through public transports, my budget is rm10,000"

config = types.GenerateContentConfig(
    system_instruction=(
        "You are a tourism agent specializing in travel planning, "
        "hotels, transportation, logistics, and events."
        "you are departing based on the latitude and longtitude provided"
        "always generate travelling route"
    ),
    tools=[types.Tool(google_maps=types.GoogleMaps(enable_widget=True))],
    tool_config=types.ToolConfig(
        retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=2.9199405250240726,
                longitude=101.6370829818403,
            )
        )
    ),
)

for model in models:
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=config,
        )
        print(f"Used {model}")
        print(response.text)
        break
    except ClientError as e:
        # Check if it's a rate limit or quota error
        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
            print(f"{model} is rate limited. Trying next model...")
            continue
        raise