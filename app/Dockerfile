FROM python:3.11-slim-buster

ENV POETRY_VERSION=1.3.1

# Install poetry
RUN pip install "poetry==$POETRY_VERSION"

# WORKDIR /app
COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false

# Install only dependencies
RUN poetry install
COPY . .
EXPOSE 8080
# ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["python", "/app/app.py"]:

