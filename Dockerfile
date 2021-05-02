FROM python:3.8

WORKDIR /usr/src/example_app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

ENTRYPOINT ["python", "./main.py"]
