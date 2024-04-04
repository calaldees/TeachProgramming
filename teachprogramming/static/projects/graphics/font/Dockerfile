FROM python:alpine
WORKDIR /app/
RUN pip install --no-cache-dir \
    pillow \
    aiohttp
COPY . .
CMD ["python", "server.py"]