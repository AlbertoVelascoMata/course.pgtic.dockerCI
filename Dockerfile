FROM python:3.8

WORKDIR /github/workspace/server

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r ./requirements.txt

ENTRYPOINT ["python", "-m", "unittest"]
