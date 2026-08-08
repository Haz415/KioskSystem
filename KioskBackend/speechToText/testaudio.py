from pathlib import Path
from dotenv import load_dotenv
from gtts import gTTS

load_dotenv()

speechToText = "क्या आप बीजिंग की यात्रा की योजना बनाने में मेरी मदद कर सकते हैं? मैं कुआलालंपुर से हूँ और मेरा बजट RM 10,000 है।"

file_name = "english.mp3"
audio_dir = Path(__file__).resolve().parent.parent / "audios"
audio_dir.mkdir(parents=True, exist_ok=True)
file_path = audio_dir / file_name

if file_path.is_file():
    print(f"'{file_name}' exists in '{audio_dir}'.")
else:
    print(f"'{file_name}' is missing from '{audio_dir}'. Generating it now.")
    speech = gTTS(text=speechToText, lang="en", slow=False)
    speech.save(str(file_path))
