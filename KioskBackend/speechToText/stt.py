from faster_whisper import WhisperModel
from .testaudio import file_path

model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=4)

segments, info = model.transcribe(str(file_path), beam_size=5)
segments = list(segments)          # <- materialize once; now it's reusable

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

full_transcript = " ".join(segment.text for segment in segments).strip()

print(repr(full_transcript))