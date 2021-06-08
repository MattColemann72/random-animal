FROM python:latest

# WORKDIR service-1

# RUN apt update
# RUN apt install python3-pip -y

# ENV SECRET_KEY=${SECRET_KEY}

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]