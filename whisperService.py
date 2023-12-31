import os
from typing import BinaryIO
import ffmpeg
import whisper
import numpy as np
from pydub import AudioSegment
from whisper.utils import get_writer

SAMPLE_RATE = 16000

async def transcribe(file, model = "small", language = "Portuguese", save_to_srt = False, filename = "transcription1"):
	
	print("Starting Transcription")
	print(f"Using Model: {model}")
	print(f"Idioma do áudio: {language}")
	print(f"Salvar transcrição em srt local: {save_to_srt}")

	if(save_to_srt):
		print(f"Filename to save: {filename}")

	audio  = load_audio(file.file)

  # define model to use
	model = whisper.load_model(model)

  # transcribe audio by passing audio data as numpy array to the model's 'transcribe' function
	result = model.transcribe(audio, word_timestamps=True, language = language)

	if(save_to_srt):
		audio_path = filename
		output_directory = "./transcriptions3"
		
		# try to create output directory
		# if directory already exists, ignore and continue code
		try: 
			os.mkdir(output_directory)
		except FileExistsError: 
			''
		except Exception: 
			raise
		
		options = {'max_line_width': 500, 'max_line_count':500, "highlight_words": False}
		srt_writer = get_writer("srt", output_directory)
		srt_writer(result, audio_path, options)

	return result

def load_audio(file: BinaryIO, encode=True, sr: int = SAMPLE_RATE):
	"""
	Open an audio file object and read as mono waveform, resampling as necessary.
	Modified from https://github.com/openai/whisper/blob/main/whisper/audio.py to accept a file object
	Parameters
	----------
	file: BinaryIO
		The audio file like object
	encode: Boolean
		If true, encode audio stream to WAV before sending to whisper
	sr: int
		The sample rate to resample the audio if necessary
	Returns
	-------
	A NumPy array containing the audio waveform, in float32 dtype.
	"""

	if encode:
		try:
			# This launches a subprocess to decode audio while down-mixing and resampling as necessary.
			# Requires the ffmpeg CLI and `ffmpeg-python` package to be installed.
			out, _ = (
				ffmpeg.input("pipe:", threads=0)
				.output("-", format="s16le", acodec="pcm_s16le", ac=1, ar=sr)
				.run(cmd="ffmpeg", capture_stdout=True, capture_stderr=True, input=file.read())
			)
		except ffmpeg.Error as e:
			raise RuntimeError(f"Failed to load audio: {e.stderr.decode()}") from e
	else:
		out = file.read()

	return np.frombuffer(out, np.int16).flatten().astype(np.float32) / 32768.0