FROM python:3.11

COPY . /root/whisper

WORKDIR /root/whisper

EXPOSE 8000

RUN apt update && apt install ffmpeg -y

RUN pip install "fastapi"
RUN pip install "uvicorn[standard]"
RUN pip install -U openai-whisper
RUN pip install "ffmpeg-python"
RUN pip install "numpy"
RUN pip install "pydub"
RUN pip install "typing"
RUN pip install "python-multipart"

CMD uvicorn main:app --port 8000 --host 0.0.0.0