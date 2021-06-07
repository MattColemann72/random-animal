FROM python

ARG SECRET_KEY

RUN apt update
RUN apt install python3-pip -y

ENV SECRET_KEY=${SECRET_KEY}

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]