FROM python:3.8

WORKDIR /github/workspace

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r ./requirements.txt

ENTRYPOINT ["python", "./src/main.py"]
