from services import generate_content
from speechToText.stt import full_transcript

def main():
    prompt = (full_transcript)
    latitude = 2.9197369417824146
    longitude = 101.63687913395918

    result = generate_content(prompt,latitude,longitude)
    print(result)

if __name__ == "__main__":
    main()