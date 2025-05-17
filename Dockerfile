FROM python:3.11-slim

WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* /app/

# Install only main dependencies (no dev)
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-root

COPY . /app

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
