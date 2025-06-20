FROM debian:11-slim

ENV PATH=/root/.local/bin:$PATH

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN apt-get update && apt-get install -y \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && curl -LsSf https://astral.sh/uv/0.5.18/install.sh | sh

RUN uv venv \
    && uv sync

EXPOSE 8000

