FROM python:3

RUN mkdir polling_app
COPY . /polling_app
WORKDIR /polling_app

RUN pip install -r requirements.txt
WORKDIR /polling_app/voting
RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]