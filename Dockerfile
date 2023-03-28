FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y python3 && \
    apt install -y python3-pip && \
    apt install -y ffmpeg && \
    apt install -y git && \
    pip3 install 'numpy<1.24.0' && \
    pip3 install torch torchvision torchaudio && \
    pip3 install git+https://github.com/openai/whisper.git 
