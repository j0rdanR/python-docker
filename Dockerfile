FROM python:3.12
LABEL org.opencontainers.image.source=https://github.com/j0rdanR/python-docker

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./main.py"]
