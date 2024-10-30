# Stage 1: Build Stage
FROM python:3.12.5-alpine3.19 AS builder
# FROM python:3.11.10-alpine3.20 AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache gcc musl-dev libffi-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

RUN find /install -type f -name '*.so*' -exec strip --strip-unneeded {} +

RUN rm -rf /install/lib/python*/site-packages/*/tests \
    /install/lib/python*/site-packages/pip* \
    /install/lib/python*/site-packages/setuptools* \
    /install/lib/python*/site-packages/wheel*

# Stage 2: Production Stage
FROM python:3.12.5-alpine3.19
# FROM gcr.io/distroless/python3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache libffi

COPY --from=builder /install /usr/local

COPY /app /app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]