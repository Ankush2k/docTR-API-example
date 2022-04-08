FROM ubuntu:latest

RUN apt update && apt upgrade -y
#RUN apt-get install -y python3-opencv
#RUN pip install opencv-python
RUN apt install --no-install-recommends ffmpeg libsm6 libxext6 -y
RUN apt install -y -q build-essential python3-pip python3-dev
#RUN apt install --no-install-recommends ffmpeg libsm6 libxext6 -y
RUN pip install -U pip setuptools wheel
RUN pip install gunicorn uvloop httptools

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY src/ /app

ENTRYPOINT /usr/local/bin/gunicorn \
 -b 0.0.0.0:80 \
 -w 4 \
 --timeout=120 \
 -k uvicorn.workers.UvicornWorker main:app \
 --chdir /app