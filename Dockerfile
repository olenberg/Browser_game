FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD flask run -h 0.0.0.0 -p 5000