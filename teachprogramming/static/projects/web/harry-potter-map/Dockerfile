FROM python:alpine
WORKDIR /app/

# Hack for python3.12 until multidict is fixed - https://stackoverflow.com/a/77806449/3356840
RUN MULTIDICT_NO_EXTENSIONS=1 pip install multidict

RUN pip install aiohttp
COPY . .
CMD ["python3", "server.py"]