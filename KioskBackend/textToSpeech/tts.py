"""import asyncio
import edge_tts
import ai.Thinking as Thinking 

VOICE = "en-US-ChristopherNeural"

async def generate_speech()-> None: 
    communicate = edge_tts.Communicate(input, VOICE)

if __name__ == "__main__":
    asyncio.run(generate_speech())
"""

from faster_whisper import WhisperModel 
from gtts import gTTS
from playsound import playsound 
import testaudio as ta

tts = gTTS(text=ta.speechToText, lang='en', slow=False)



print("Audio file 'whisper_test.mp3' has been generated in your current directory.")

model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=4)
segments, info = model.transcribe("audio.mp3", beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

playsound("audio.mp3")