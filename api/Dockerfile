FROM python:3.11-alpine

WORKDIR /api
COPY ./requirements.txt /api/requirements.txt

RUN pip install -r requirements.txt

COPY . /api

RUN coverage run -m pytest

RUN coverage report -m

CMD ["fastapi", "run", "main/main.py", "--port", "8080"]
