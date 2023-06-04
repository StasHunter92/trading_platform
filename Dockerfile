FROM python:3.10-slim

WORKDIR /trading_platform_api

ENV PYTHONUNBUFFERED=1

RUN pip install poetry

COPY pyproject.toml .
COPY pytest.ini .
COPY api/. ./api
COPY core/. ./core
COPY tests/. ./tests
COPY trading_platform/. ./trading_platform

COPY manage.py .

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-root

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]