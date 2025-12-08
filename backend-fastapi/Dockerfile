FROM python:3.12-slim-bookworm

WORKDIR /app/backend

COPY . .

RUN pip install .

EXPOSE 8080

CMD ["python", "main.py"]