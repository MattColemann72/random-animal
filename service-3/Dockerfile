FROM python:latest

# ENV SECRET_KEY=${SECRET_KEY}

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5002

ENTRYPOINT ["python3", "app.py"]