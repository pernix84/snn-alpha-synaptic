from python:3.10.9-sli

COPY . /app
WORKDIR /app

RUN python -m pip install requirements.txt

ENTRYPOINT [ "pytest" ]
