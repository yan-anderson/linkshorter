FROM python:3.8.2

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP "app.py"

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY src /usr/src/app
EXPOSE 5000

RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]
