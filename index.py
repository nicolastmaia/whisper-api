import whisper
import numpy as np
import soundfile as sf
from pydub import AudioSegment
from whisper.utils import get_writer

# define model to use
model = whisper.load_model("small")

# path of the audio file to transcribe
audio_path = "audio.mp3"

# path where to save transcription
output_directory = "."

# read audio as AudioSegment object
audioSegment = AudioSegment.from_file(audio_path)

# convert AudioSegment object to numpy array
data = np.frombuffer(audioSegment.raw_data, np.int16).flatten().astype(np.float32) / 32768.0

# transcribe audio by passing audio data as numpy array to the model's 'transcribe' function
result = model.transcribe(data)

# print transcription on console without line breaks
print(result["text"])

# get object to write transcription as a srt file
srt_writer = get_writer("srt", output_directory)

# save as a SRT file with hard line breaks
srt_writer(result, audio_path, {'max_line_width': 500, 'max_line_count':500, "highlight_words": False,
})