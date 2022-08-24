FROM python:3.10.6

WORKDIR /app


ENV PYTHOUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


COPY . /app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]