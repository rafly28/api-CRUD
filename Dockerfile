# Stage 1: Build Stage
FROM python:3.12.5-alpine3.19 as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install build dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev

# Create working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Strip unnecessary files to reduce size
RUN find /install -type f -name '*.so*' -exec strip --strip-unneeded {} +

# Remove unneeded files from dependencies
RUN rm -rf /install/lib/python*/site-packages/*/tests \
    /install/lib/python*/site-packages/pip* \
    /install/lib/python*/site-packages/setuptools* \
    /install/lib/python*/site-packages/wheel*

# Stage 2: Production Stage
FROM python:3.12.5-alpine3.19

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install runtime dependencies
RUN apk add --no-cache libffi

# Create working directory
WORKDIR /app

# Copy installed dependencies from builder stage
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
