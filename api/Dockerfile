# api/Dockerfile
FROM python:3.13-slim-bookworm


# Set Poetry and Pyton Environment
ENV PYTHONUNBUFFERED=1
ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"


# Application Arguments from docker-compose and Set Application Environment
ARG APP_ENVIRONMENT=unknown
ARG APP_DEBUG=false
ENV APP_ENVIRONMENT=$APP_ENVIRONMENT
ENV APP_DEBUG=$APP_DEBUG
ARG ARG_COPY_FROM=./README.md
ARG ARG_COPY_DEST=./README.md


# Set Work Directory
WORKDIR /app


# Install Poetry (https://python-poetry.org/docs/#installing-with-the-official-installer)
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -


# Copy toml setting file and poetry.lock into WORKDIR
COPY pyproject.toml poetry.lock ./


# Copy README.md (for all) and Source files (for Production only via Arguments from docker compose)
COPY ./README.md ./README.md
COPY ${ARG_COPY_FROM} ${ARG_COPY_DEST}


# Check and Installing dependencies
RUN poetry config virtualenvs.create false && \
    if [ "$APP_ENVIRONMENT" = "prod" ]; then \
        echo "Installing dependencies for prod"; \
        poetry install --no-cache --no-root; \
    else \
        echo "Installing dependencies for dev"; \
        poetry install --no-root; \
    fi


# Open port
EXPOSE 8000
