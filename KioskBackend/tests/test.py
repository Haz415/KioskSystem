from client import client


interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)

import itertools

API_KEYS = ["key_A", "key_B", "key_C"]
_key_cycle = itertools.cycle(API_KEYS)

def get_fresh_key():
    return next(_key_cycle)

# each request can grab the next key
client = genai.Client(api_key=get_fresh_key())


API_KEYS = ["GEMINI_API_KEY1","GEMINI_API_KEY2"]
_key_cycle =itertools.cycle(API_KEYS)

def get_fresh_key():
    return next(_key_cycle)

# each request can grab the next key
client = genai.Client(api_key=get_fresh_key())
