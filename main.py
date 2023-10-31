from fastapi import FastAPI, UploadFile
import whisperService

app = FastAPI()

# OBS.: Works with .wav better than with .mp3 (no matter sample size or bit rate)
@app.post("/v1/transcribe")
async def transcribe(file: UploadFile):
	result = await whisperService.transcribe(file)
	return result