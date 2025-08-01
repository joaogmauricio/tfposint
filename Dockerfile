FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/db/data

ENV DATABASE_URL=sqlite:///core/database/data/tfposint.db

CMD ["python", "tfposint.py"]
