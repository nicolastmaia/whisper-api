import whisper


model = whisper.load_model("small")
audio = "../test-audio/audio.mp3"
result = model.transcribe(audio)


with open("../test-audio/transcription.txt", "w", encoding="utf-8") as txt:
    txt.write(result["text"])