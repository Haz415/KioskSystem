from google.genai import types
from google.genai.errors import ClientError

models = [
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
    "gemini-3-flash-preview",
]

SYSTEM_INSTRUCTION = (
        "You are a travel agent help",
        "Output in English", 
        "Provide overview of the trip planning"
        "Be direct"
    )

def build_config(latitude, longitude):
    return types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        tools=[types.Tool(google_maps=types.GoogleMaps(enable_widget=True))],
        tool_config=types.ToolConfig(
            retrieval_config=types.RetrievalConfig(
                lat_lng=types.LatLng(latitude=latitude, longitude=longitude)
            )
        ),
    )