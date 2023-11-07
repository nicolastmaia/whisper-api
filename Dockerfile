FROM whisper-api

WORKDIR /root/whisper

EXPOSE 8000

CMD uvicorn main:app --port 8000 --host 0.0.0.0