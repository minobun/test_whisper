FROM ubuntu:20.04

COPY app /app
WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y ffmpeg
RUN apt install -y git
RUN pip3 install 'numpy<1.24.0'
RUN pip3 install torch torchvision torchaudio
RUN pip3 install git+https://github.com/openai/whisper.git 
