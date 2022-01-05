# =============================================================================
# Base
# =============================================================================
FROM python:3.9 AS base
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock /app/

# =============================================================================
# Development
# =============================================================================
FROM base as development
RUN poetry config virtualenvs.create false  && \
    poetry install --no-interaction --no-ansi
COPY . /app/
RUN chmod +x /app/*.sh
CMD ["sh", "setup_dev.sh"]
