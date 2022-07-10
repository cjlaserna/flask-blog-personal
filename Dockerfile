FROM python:3.10-slim-buster

WORKDIR /flask-blog-personal

RUN ls

COPY poetry.lock .

COPY pyproject.toml .

ENV POETRY_VERSION=1.1.13

RUN python3 -m pip install poetry==$POETRY_VERSION

RUN poetry config virtualenvs.in-project true --local

RUN poetry update

RUN poetry install

COPY . .

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
