FROM python:3.10

WORKDIR /app

COPY . .

EXPOSE 8000

CMD ["python3", "app.py"]