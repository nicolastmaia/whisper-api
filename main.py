from fastapi import FastAPI, UploadFile, Form
import whisperService
from typing import Annotated

app = FastAPI()

# OBS.: Works better with .wav than with .mp3 (no matter sample size or bit rate)
@app.post("/v1/transcribe")
async def transcribe(file: UploadFile, model: Annotated[str | None, Form()], language: Annotated[str | None, Form()], save_to_srt: Annotated[bool | None, Form()], filename: Annotated[str | None, Form()]):
	result = await whisperService.transcribe(file, model, language, save_to_srt, filename)
	return result