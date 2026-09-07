ARG PYTHON_IMAGE=python:3.12-slim
FROM ${PYTHON_IMAGE}

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements-runtime.txt /tmp/requirements-runtime.txt
RUN pip install --no-cache-dir -r /tmp/requirements-runtime.txt
COPY services/request-api/request_api /app/request_api
COPY database/migrations/request-db /app/migrations

USER 65532:65532
EXPOSE 8000
CMD ["uvicorn", "request_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
