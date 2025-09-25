FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
    && if [ -f pyproject.toml ]; then pip install --no-cache-dir .; \
    elif [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; \
    fi

COPY . .

CMD ["python", "-m", "app.main"]
