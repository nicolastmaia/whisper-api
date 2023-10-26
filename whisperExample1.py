import os
import whisper
import numpy as np
from pydub import AudioSegment
from whisper.utils import get_writer

def transcribe():
  # define model to use
  model = whisper.load_model("small")

  # path of the audio file to transcribe
  audio_path = "audio2.mp3"

  # path where to save transcription
  output_directory = "./transcriptions1"

  # try to create output directory
  # if directory already exists, ignore and continue code
  try: 
    os.mkdir(output_directory)
  except FileExistsError: 
    ''
  except Exception: 
    raise

  # transcribe audio by passing audio data as numpy array to the model's 'transcribe' function
  result = model.transcribe(audio_path)

  # print transcription on console without line breaks
  print(result["text"])

  # build options for  transcription writer objects
  options = {'max_line_width': 500, 'max_line_count':500, "highlight_words": False}

  # get objects to write transcription as different files
  txt_writer = get_writer("txt", output_directory)
  json_writer = get_writer("json",  output_directory)
  vtt_writer = get_writer("vtt", output_directory)
  tsv_writer = get_writer("tsv", output_directory)
  srt_writer = get_writer("srt", output_directory)

  # save transcription in different format files
  txt_writer(result, audio_path, options)
  json_writer(result, audio_path, options)
  vtt_writer(result, audio_path, options)
  tsv_writer(result, audio_path, options)
  srt_writer(result, audio_path, options)

transcribe()