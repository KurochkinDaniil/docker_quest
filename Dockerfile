FROM python:3.10

ARG FASTAPI_ENV

ENV FASTAPI_ENV=${FASTAPI_ENV}\
  PYTHONFAULTHANDLER=1\
  PYTHONUNBUFFERED=1\
  PYTHONHASHSEED=random\
  PIP_NO_CACHE_DIR=off\
  PIP_DISABLE_PIP_VERSION_CHECK=on\
  PIP_DEFAULT_TIMEOUT=100\
  POETRY_VERSION=1.0.0


RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /code

COPY poetry.lock pyproject.toml /code/
COPY app/main.py /code/
COPY app/services.py /code/
COPY app/static/step1.html /code/
COPY app/static/step2.html /code/
COPY app/static/step3.html /code/
COPY app/files/answer.txt /code/app/files/

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$FASTAPI_ENV" == production && echo "--no-dev") --no-interaction --no-ansi
CMD ["python", "/code/app/services.py"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
COPY crypto.key /code/
COPY . /code